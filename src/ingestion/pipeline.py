from pathlib import Path

from .csv_loader import load_csv, save_processed


DATASETS = [
    "customers.csv",
    "products.csv",
    "orders.csv",
    "order_items.csv",
    "payments.csv",
    "shipments.csv",
]


def run_ingestion() -> None:
    """
    Load all raw CSV datasets and write them
    to the processed data directory.
    """

    for dataset in DATASETS:
        print(f"Ingesting {dataset}...")

        dataframe = load_csv(dataset)

        output_name = Path(dataset).name

        save_processed(
            dataframe,
            output_name,
        )

        print(
            f"Completed {dataset}: "
            f"{len(dataframe)} rows"
        )


if __name__ == "__main__":
    run_ingestion()
