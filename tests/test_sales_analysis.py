
"""Tests for restaurant sales analysis functions."""

import pandas as pd

from src.sales_analysis import (
    calculate_revenue,
    total_revenue,
    revenue_by_item,
    quantity_by_item,
)


def sample_sales_data() -> pd.DataFrame:
    """Create a small dataset with known expected results."""
    return pd.DataFrame(
        {
            "Date": ["2026-10-01", "2026-10-01", "2026-10-02"],
            "Item": ["Paneer Tikka", "Dal Makhani", "Paneer Tikka"],
            "Category": ["Starter", "Main Course", "Starter"],
            "Quantity": [10, 5, 2],
            "Price": [220, 280, 220],
        }
    )


def test_calculate_revenue():
    df = sample_sales_data()
    result = calculate_revenue(df)

    assert result["Revenue"].tolist() == [2200, 1400, 440]
    assert "Revenue" not in df.columns


def test_total_revenue():
    df = sample_sales_data()

    assert total_revenue(df) == 4040.0


def test_revenue_by_item():
    df = sample_sales_data()
    result = revenue_by_item(df)

    assert result.iloc[0]["Item"] == "Paneer Tikka"
    assert result.iloc[0]["Revenue"] == 2640


def test_quantity_by_item():
    df = sample_sales_data()
    result = quantity_by_item(df)

    assert result.iloc[0]["Item"] == "Paneer Tikka"
    assert result.iloc[0]["Quantity"] == 12

from src.data_cleaning import clean_sales_data


def test_clean_sales_data_removes_duplicates():
    """Exact duplicate records should be removed."""
    df = sample_sales_data()
    df = pd.concat([df, df.iloc[[0]]], ignore_index=True)

    result = clean_sales_data(df)

    assert len(result) == 3


def test_clean_sales_data_removes_invalid_rows():
    """Rows with invalid dates or non-positive quantities are removed."""
    df = pd.DataFrame(
        {
            "Date": ["2026-10-01", "invalid-date", "2026-10-02"],
            "Item": ["Paneer Tikka", "Dal Makhani", "Gulab Jamun"],
            "Category": ["Starter", "Main Course", "Dessert"],
            "Quantity": [2, 5, 0],
            "Price": [220, 280, 80],
        }
    )

    result = clean_sales_data(df)

    assert len(result) == 1
    assert result.iloc[0]["Item"] == "Paneer Tikka"


def test_clean_sales_data_rejects_missing_columns():
    """Missing required columns should produce a clear error."""
    df = pd.DataFrame({"Item": ["Paneer Tikka"]})

    try:
        clean_sales_data(df)
    except ValueError as error:
        assert "Missing required columns" in str(error)
    else:
        raise AssertionError("Expected ValueError for missing columns")
