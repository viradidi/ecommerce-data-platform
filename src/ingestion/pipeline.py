import logging
from pathlib import Path

from ..quality.orders import validate_orders
from ..utils.logging_config import configure_logging
from .csv_loader import load_csv, save_processed


logger = logging.getLogger(__name__)


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

    logger.info("Starting ingestion pipeline")

    for dataset in DATASETS:
        logger.info("Ingesting %s", dataset)

        dataframe = load_csv(dataset)

        if dataset == "orders.csv":
            logger.info("Validating orders dataset")
            validate_orders(dataframe)
            logger.info("Orders validation passed")

        output_name = Path(dataset).name

        save_processed(
            dataframe,
            output_name,
        )

        logger.info(
            "Completed %s | rows=%s",
            dataset,
            len(dataframe),
        )

    logger.info("Ingestion pipeline completed successfully")


if __name__ == "__main__":
    configure_logging()
    run_ingestion()
