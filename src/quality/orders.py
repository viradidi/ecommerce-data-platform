import pandas as pd

from .validator import (
    validate_not_null,
    validate_positive,
    validate_required_columns,
    validate_unique,
)


def validate_orders(dataframe: pd.DataFrame) -> None:
    """
    Run all quality checks required for the orders dataset.
    """

    validate_required_columns(
        dataframe,
        [
            "order_id",
            "customer_id",
            "product_id",
            "quantity",
            "order_date",
            "status",
            "total_amount",
        ],
    )

    validate_not_null(
        dataframe,
        [
            "order_id",
            "customer_id",
            "product_id",
            "status",
        ],
    )

    validate_unique(
        dataframe,
        "order_id",
    )

    validate_positive(
        dataframe,
        [
            "quantity",
            "total_amount",
        ],
    )
