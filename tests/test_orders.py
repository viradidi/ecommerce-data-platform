import pandas as pd
import pytest

from src.quality.orders import validate_orders


def valid_orders() -> pd.DataFrame:
    return pd.DataFrame(
        {
            "order_id": [1001, 1002],
            "customer_id": [1, 2],
            "product_id": [1, 2],
            "quantity": [1, 2],
            "order_date": [
                "2026-02-01",
                "2026-02-02",
            ],
            "status": [
                "Completed",
                "Completed",
            ],
            "total_amount": [1200.00, 70.00],
        }
    )


def test_valid_orders_pass():
    dataframe = valid_orders()

    validate_orders(dataframe)


def test_duplicate_order_id_fails():
    dataframe = valid_orders()

    dataframe.loc[1, "order_id"] = 1001

    with pytest.raises(ValueError):
        validate_orders(dataframe)


def test_missing_required_column_fails():
    dataframe = valid_orders()

    dataframe = dataframe.drop(
        columns=["customer_id"]
    )

    with pytest.raises(ValueError):
        validate_orders(dataframe)


def test_negative_quantity_fails():
    dataframe = valid_orders()

    dataframe.loc[0, "quantity"] = -1

    with pytest.raises(ValueError):
        validate_orders(dataframe)
