from datetime import datetime
from decimal import Decimal
from pathlib import Path
import csv

from airflow.sdk import DAG, task
from airflow.providers.standard.operators.bash import BashOperator
from airflow.providers.postgres.hooks.postgres import PostgresHook


# -------------------------------------------------------------------
# Configuration
# -------------------------------------------------------------------

DATA_FILE = Path("/opt/airflow/data/customer_transactions.csv")
POSTGRES_CONN_ID = "data_platform_postgres"

TARGET_TABLE = "customer_transactions"


# -------------------------------------------------------------------
# DAG
# -------------------------------------------------------------------

with DAG(
    dag_id="daily_platform_pipeline",
    start_date=datetime(2026, 8, 1),
    schedule="@daily",
    catchup=False,
    tags=[
        "portfolio",
        "postgres",
        "etl",
        "dbt",
        "data-quality",
    ],
    description="End-to-end customer transaction data pipeline",
) as dag:

    # ---------------------------------------------------------------
    # EXTRACT
    # ---------------------------------------------------------------

    @task
    def extract():
        """
        Extract customer transactions from the source CSV.
        """

        if not DATA_FILE.exists():
            raise FileNotFoundError(
                f"Source file not found: {DATA_FILE}"
            )

        records = []

        with DATA_FILE.open(
            "r",
            newline="",
            encoding="utf-8",
        ) as file:

            reader = csv.DictReader(file)

            required_columns = {
                "customer_id",
                "customer_name",
                "amount",
            }

            if not required_columns.issubset(
                reader.fieldnames or []
            ):
                raise ValueError(
                    f"CSV is missing required columns. "
                    f"Expected: {required_columns}. "
                    f"Found: {reader.fieldnames}"
                )

            for row_number, row in enumerate(
                reader,
                start=2,
            ):

                try:
                    record = {
                        "customer_id": int(
                            row["customer_id"]
                        ),
                        "customer_name": row[
                            "customer_name"
                        ].strip(),
                        "amount": Decimal(
                            row["amount"]
                        ),
                    }

                except (TypeError, ValueError) as exc:

                    raise ValueError(
                        f"Invalid data on CSV row "
                        f"{row_number}: {row}"
                    ) from exc

                records.append(record)

        print(
            f"Extracted {len(records)} records "
            f"from {DATA_FILE}"
        )

        return records

    # ---------------------------------------------------------------
    # VALIDATE
    # ---------------------------------------------------------------

    @task
    def validate(records):
        """
        Perform data-quality validation before loading.
        """

        if not records:
            raise ValueError(
                "Source returned zero records"
            )

        required_columns = {
            "customer_id",
            "customer_name",
            "amount",
        }

        customer_ids = set()

        for record in records:

            # Check required fields
            missing_columns = (
                required_columns - record.keys()
            )

            if missing_columns:
                raise ValueError(
                    f"Missing columns: {missing_columns}"
                )

            customer_id = record["customer_id"]
            customer_name = record["customer_name"]
            amount = record["amount"]

            # Validate customer ID
            if customer_id is None:
                raise ValueError(
                    "customer_id cannot be NULL"
                )

            if customer_id <= 0:
                raise ValueError(
                    f"customer_id must be positive: "
                    f"{customer_id}"
                )

            # Validate uniqueness
            if customer_id in customer_ids:
                raise ValueError(
                    f"Duplicate customer_id: "
                    f"{customer_id}"
                )

            customer_ids.add(customer_id)

            # Validate customer name
            if not customer_name:
                raise ValueError(
                    f"customer_name cannot be empty "
                    f"for customer {customer_id}"
                )

            # Validate amount
            if amount is None:
                raise ValueError(
                    f"amount cannot be NULL "
                    f"for customer {customer_id}"
                )

            if amount < Decimal("0"):
                raise ValueError(
                    f"Negative amount for customer "
                    f"{customer_id}: {amount}"
                )

        print(
            f"Validation passed for "
            f"{len(records)} records"
        )

        return records

    # ---------------------------------------------------------------
    # LOAD
    # ---------------------------------------------------------------

    @task
    def load(records):
        """
        Idempotently load validated records into PostgreSQL.

        Uses customer_id as the business key so rerunning
        the pipeline updates existing records instead of
        creating duplicates.
        """

        hook = PostgresHook(
            postgres_conn_id=POSTGRES_CONN_ID
        )

        # Create target table if it does not exist.
        create_table_sql = f"""
        CREATE TABLE IF NOT EXISTS {TARGET_TABLE} (
            customer_id INTEGER PRIMARY KEY,
            customer_name TEXT NOT NULL,
            amount NUMERIC(12, 2) NOT NULL,
            loaded_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
        );
        """

        hook.run(create_table_sql)

        # Idempotent upsert.
        insert_sql = f"""
        INSERT INTO {TARGET_TABLE} (
            customer_id,
            customer_name,
            amount
        )
        VALUES (%s, %s, %s)
        ON CONFLICT (customer_id)
        DO UPDATE SET
            customer_name = EXCLUDED.customer_name,
            amount = EXCLUDED.amount,
            loaded_at = CURRENT_TIMESTAMP;
        """

        for record in records:

            hook.run(
                insert_sql,
                parameters=(
                    record["customer_id"],
                    record["customer_name"],
                    record["amount"],
                ),
            )

        print(
            f"Successfully loaded "
            f"{len(records)} records "
            f"into {TARGET_TABLE}"
        )

    # ---------------------------------------------------------------
    # DBT BUILD
    # ---------------------------------------------------------------

    dbt_build = BashOperator(
        task_id="dbt_build",
        bash_command=(
            "cd /opt/airflow/dbt && "
            "dbt build "
            "--profiles-dir /opt/airflow/dbt"
        ),
    )

    # ---------------------------------------------------------------
    # PIPELINE DEPENDENCIES
    # ---------------------------------------------------------------

    extracted = extract()

    validated = validate(extracted)

    load_task = load(validated)

    load_task >> dbt_build