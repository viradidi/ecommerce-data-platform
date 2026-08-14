from pathlib import Path

import yaml


PROJECT_ROOT = Path(__file__).resolve().parents[2]
CONFIG_PATH = PROJECT_ROOT / "config" / "config.yaml"


def load_config() -> dict:
    """
    Load application configuration from config.yaml.
    """

    if not CONFIG_PATH.exists():
        raise FileNotFoundError(
            f"Configuration file not found: {CONFIG_PATH}"
        )

    with CONFIG_PATH.open("r", encoding="utf-8") as file:
        return yaml.safe_load(file)