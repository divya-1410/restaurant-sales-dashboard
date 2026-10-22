
"""Functions for loading restaurant sales data."""

from pathlib import Path

import pandas as pd


PROJECT_ROOT = Path(__file__).resolve().parent.parent
DATA_FILE = PROJECT_ROOT / "data" / "restaurant_sales.csv"


def load_sales_data(file_path: Path = DATA_FILE) -> pd.DataFrame:
    """Load restaurant sales data from a CSV file."""
    return pd.read_csv(file_path)
