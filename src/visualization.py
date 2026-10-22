
"""Functions for creating restaurant sales charts."""

from pathlib import Path

import matplotlib
matplotlib.use("Agg")

import matplotlib.pyplot as plt
import pandas as pd


def plot_revenue_by_item(
    sales_df: pd.DataFrame,
    output_path: Path,
) -> None:
    """Save a bar chart showing revenue by menu item."""
    revenue = (
        sales_df.groupby("Item")["Revenue"]
        .sum()
        .sort_values(ascending=False)
    )

    output_path.parent.mkdir(parents=True, exist_ok=True)

    fig, ax = plt.subplots(figsize=(9, 5))
    revenue.plot(kind="bar", ax=ax)

    ax.set_title("Revenue by Menu Item")
    ax.set_xlabel("Menu Item")
    ax.set_ylabel("Revenue (Rs.)")
    ax.tick_params(axis="x", rotation=30)

    fig.tight_layout()
    fig.savefig(output_path, dpi=150)
    plt.close(fig)


def plot_daily_revenue(
    sales_df: pd.DataFrame,
    output_path: Path,
) -> None:
    """Save a line chart showing revenue by date."""
    daily = (
        sales_df.groupby("Date")["Revenue"]
        .sum()
        .sort_index()
    )

    output_path.parent.mkdir(parents=True, exist_ok=True)

    fig, ax = plt.subplots(figsize=(9, 5))
    ax.plot(daily.index, daily.values, marker="o")

    ax.set_title("Daily Restaurant Revenue")
    ax.set_xlabel("Date")
    ax.set_ylabel("Revenue (Rs.)")
    fig.autofmt_xdate()

    fig.tight_layout()
    fig.savefig(output_path, dpi=150)
    plt.close(fig)
