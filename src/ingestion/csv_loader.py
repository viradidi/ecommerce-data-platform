from pathlib import Path

import pandas as pd


PROJECT_ROOT = Path(__file__).resolve().parents[2]

RAW_DATA_DIR = PROJECT_ROOT / "data" / "raw"
PROCESSED_DATA_DIR = PROJECT_ROOT / "data" / "processed"


def load_csv(file_name: str) -> pd.DataFrame:
    """
    Load a CSV file from the raw data directory.

    Parameters
    ----------
    file_name:
        Name of the CSV file.

    Returns
    -------
    pd.DataFrame:
        Loaded source data.

    Raises
    ------
    FileNotFoundError:
        If the requested source file does not exist.
    """

    file_path = RAW_DATA_DIR / file_name

    if not file_path.exists():
        raise FileNotFoundError(
            f"Source file not found: {file_path}"
        )

    return pd.read_csv(file_path)


def save_processed(
    df: pd.DataFrame,
    file_name: str,
) -> None:
    """
    Save a DataFrame to the processed data directory.
    """

    PROCESSED_DATA_DIR.mkdir(
        parents=True,
        exist_ok=True,
    )

    output_path = PROCESSED_DATA_DIR / file_name

    df.to_csv(
        output_path,
        index=False,
    )
