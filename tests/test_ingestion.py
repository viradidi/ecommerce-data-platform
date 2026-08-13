import pytest

from src.ingestion.pipeline import ingest_dataset


def test_ingest_orders():
    row_count = ingest_dataset("orders.csv")

    assert row_count == 15


def test_missing_dataset_fails():
    with pytest.raises(FileNotFoundError):
        ingest_dataset("does_not_exist.csv")
