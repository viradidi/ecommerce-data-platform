from pathlib import Path

from .csv_loader import load_csv, save_processed
from ..quality.orders import validate_orders


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
    Load raw datasets, validate them, and save
    validated datasets to the processed layer.
    """

    for dataset in DATASETS:
        print(f"Ingesting {dataset}...")

        dataframe = load_csv(dataset)

        if dataset == "orders.csv":
            print("Validating orders...")
            validate_orders(dataframe)
            print("Orders validation passed.")

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
