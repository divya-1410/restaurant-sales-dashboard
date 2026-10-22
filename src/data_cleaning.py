
"""Functions for validating and cleaning restaurant sales data."""

import pandas as pd


REQUIRED_COLUMNS = ["Date", "Item", "Category", "Quantity", "Price"]


def clean_sales_data(df: pd.DataFrame) -> pd.DataFrame:
    """Validate, clean, and return a copy of the sales data."""
    cleaned_df = df.copy()

    # Check that all required columns are present.
    missing_columns = [
        column for column in REQUIRED_COLUMNS
        if column not in cleaned_df.columns
    ]
    if missing_columns:
        raise ValueError(f"Missing required columns: {missing_columns}")

    # Remove rows that are exact duplicates.
    cleaned_df = cleaned_df.drop_duplicates()

    # Remove rows with missing values in required columns.
    cleaned_df = cleaned_df.dropna(subset=REQUIRED_COLUMNS)

    # Convert values to their expected data types.
    cleaned_df["Date"] = pd.to_datetime(
        cleaned_df["Date"], errors="coerce"
    )
    cleaned_df["Quantity"] = pd.to_numeric(
        cleaned_df["Quantity"], errors="coerce"
    )
    cleaned_df["Price"] = pd.to_numeric(
        cleaned_df["Price"], errors="coerce"
    )

    # Remove rows with invalid dates or numeric values.
    cleaned_df = cleaned_df.dropna(subset=REQUIRED_COLUMNS)

    # Keep only sensible positive quantities and non-negative prices.
    cleaned_df = cleaned_df[
        (cleaned_df["Quantity"] > 0)
        & (cleaned_df["Price"] >= 0)
    ]

    return cleaned_df.reset_index(drop=True)
