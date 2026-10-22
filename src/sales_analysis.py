
"""Functions for analysing restaurant sales data."""

import pandas as pd


def calculate_revenue(df: pd.DataFrame) -> pd.DataFrame:
    """Return a copy of the sales data with calculated revenue."""
    result = df.copy()
    result["Revenue"] = result["Quantity"] * result["Price"]
    return result


def total_revenue(df: pd.DataFrame) -> float:
    """Calculate total revenue across all sales."""
    sales = calculate_revenue(df)
    return float(sales["Revenue"].sum())


def revenue_by_item(df: pd.DataFrame) -> pd.DataFrame:
    """Calculate total revenue for each menu item."""
    sales = calculate_revenue(df)
    return (
        sales.groupby("Item", as_index=False)["Revenue"]
        .sum()
        .sort_values("Revenue", ascending=False)
        .reset_index(drop=True)
    )


def quantity_by_item(df: pd.DataFrame) -> pd.DataFrame:
    """Calculate total quantity sold for each menu item."""
    return (
        df.groupby("Item", as_index=False)["Quantity"]
        .sum()
        .sort_values("Quantity", ascending=False)
        .reset_index(drop=True)
    )


def revenue_by_category(df: pd.DataFrame) -> pd.DataFrame:
    """Calculate total revenue for each food category."""
    sales = calculate_revenue(df)
    return (
        sales.groupby("Category", as_index=False)["Revenue"]
        .sum()
        .sort_values("Revenue", ascending=False)
        .reset_index(drop=True)
    )


def daily_revenue(df: pd.DataFrame) -> pd.DataFrame:
    """Calculate total revenue for each date."""
    sales = calculate_revenue(df)
    return (
        sales.groupby("Date", as_index=False)["Revenue"]
        .sum()
        .sort_values("Date")
        .reset_index(drop=True)
    )
