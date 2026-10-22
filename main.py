
"""Main entry point for the Restaurant Sales Dashboard."""

from pathlib import Path

from src.data_loader import load_sales_data
from src.data_cleaning import clean_sales_data
from src.sales_analysis import (
    calculate_revenue,
    total_revenue,
    revenue_by_item,
    quantity_by_item,
    revenue_by_category,
    daily_revenue,
)
from src.visualization import (
    plot_revenue_by_item,
    plot_daily_revenue,
)


PROJECT_ROOT = Path(__file__).resolve().parent
OUTPUT_DIR = PROJECT_ROOT / "outputs"


def main() -> None:
    """Run the restaurant sales analysis workflow."""
    print("=" * 50)
    print("RESTAURANT SALES DASHBOARD")
    print("=" * 50)

    # Load and clean the dataset.
    sales_df = load_sales_data()
    cleaned_df = clean_sales_data(sales_df)

    print(f"\nRecords loaded: {len(sales_df)}")
    print(f"Records after cleaning: {len(cleaned_df)}")

    # Calculate and display key metrics.
    revenue_df = calculate_revenue(cleaned_df)

    print(f"\nTotal revenue: Rs. {total_revenue(cleaned_df):,.2f}")

    print("\nRevenue by menu item:")
    print(revenue_by_item(cleaned_df).to_string(index=False))

    print("\nQuantity sold by menu item:")
    print(quantity_by_item(cleaned_df).to_string(index=False))

    print("\nRevenue by category:")
    print(revenue_by_category(cleaned_df).to_string(index=False))

    print("\nDaily revenue:")
    print(daily_revenue(cleaned_df).to_string(index=False))

    # Generate and save charts.
    plot_revenue_by_item(
        revenue_df,
        OUTPUT_DIR / "revenue_by_item.png",
    )
    plot_daily_revenue(
        revenue_df,
        OUTPUT_DIR / "daily_revenue.png",
    )

    print(f"\nCharts saved in: {OUTPUT_DIR}")
    print("\nAnalysis completed successfully!")


if __name__ == "__main__":
    main()
