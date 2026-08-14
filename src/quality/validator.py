from typing import Iterable

import pandas as pd


def validate_required_columns(
    dataframe: pd.DataFrame,
    required_columns: Iterable[str],
) -> None:
    """
    Validate that all required columns exist.
    """

    missing_columns = [
        column
        for column in required_columns
        if column not in dataframe.columns
    ]

    if missing_columns:
        raise ValueError(
            f"Missing required columns: {missing_columns}"
        )


def validate_not_null(
    dataframe: pd.DataFrame,
    columns: Iterable[str],
) -> None:
    """
    Validate that specified columns contain no null values.
    """

    null_columns = [
        column
        for column in columns
        if dataframe[column].isnull().any()
    ]

    if null_columns:
        raise ValueError(
            f"Null values found in columns: {null_columns}"
        )


def validate_unique(
    dataframe: pd.DataFrame,
    column: str,
) -> None:
    """
    Validate that a column contains unique values.
    """

    if dataframe[column].duplicated().any():
        raise ValueError(
            f"Duplicate values found in column: {column}"
        )


def validate_positive(
    dataframe: pd.DataFrame,
    columns: Iterable[str],
) -> None:
    """
    Validate that specified numeric columns contain
    only positive values.
    """

    invalid_columns = [
        column
        for column in columns
        if (dataframe[column] <= 0).any()
    ]

    if invalid_columns:
        raise ValueError(
            f"Non-positive values found in columns: "
            f"{invalid_columns}"
        )
