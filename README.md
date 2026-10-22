# Restaurant Sales Dashboard

A Python-based restaurant sales analysis and visualization project that calculates revenue, analyses menu-item performance, and generates charts from restaurant sales data.

## Project Overview

Restaurants need to understand which menu items generate the most revenue, which items sell in the largest quantities, and how sales change over time.

This project uses Python to clean restaurant sales data, calculate useful business metrics, and generate visualizations that make the results easier to understand.

**Note:** This is currently a command-line analysis application that generates chart images, not an interactive web dashboard.

## Features

- Load sales data from a CSV file.
- Validate and clean the dataset.
- Calculate revenue for individual sales records.
- Calculate total restaurant revenue.
- Analyse revenue by menu item and category.
- Analyse quantities sold by menu item.
- Calculate daily revenue.
- Generate and save revenue charts.
- Run automated tests using pytest.

## Technologies Used

- Python
- pandas
- Matplotlib
- pytest
- CSV data processing
- Git and GitHub

## Project Structure

```text
restaurant-sales-dashboard/
├── data/
│   └── restaurant_sales.csv
├── docs/
│   ├── screenshots/
│   ├── data_dictionary.md
│   └── test_cases.md
├── outputs/
│   ├── README.md
│   ├── revenue_by_item.png
│   └── daily_revenue.png
├── src/
│   ├── __init__.py
│   ├── data_loader.py
│   ├── data_cleaning.py
│   ├── sales_analysis.py
│   └── visualization.py
├── tests/
│   └── test_sales_analysis.py
├── .gitignore
├── main.py
└── requirements.txt
```

## Requirements

- Python 3.10 or newer
- pip
- Git (for cloning the repository)

## Installation and Setup

### 1. Clone the repository

```bash
git clone https://github.com/divya-1410/restaurant-sales-dashboard.git
cd restaurant-sales-dashboard
```

### 2. Create a virtual environment

**Windows:**

```powershell
py -m venv .venv
.\.venv\Scripts\Activate.ps1
```

If PowerShell blocks activation, use an appropriate temporary execution-policy adjustment or activate the environment through another supported terminal.

### 3. Install dependencies

```bash
py -m pip install -r requirements.txt
```

### 4. Run the project

```bash
py main.py
```

The program prints sales-analysis results in the terminal and generates the following chart files in the `outputs/` directory:

- `revenue_by_item.png`
- `daily_revenue.png`

### 5. Run automated tests

```bash
py -m pytest tests/ -v
```

## Sample Dataset

The included demonstration dataset contains six sales records across two dates.

The following results are calculated from this sample data:

| Metric | Result |
|---|---:|
| Total revenue | ₹15,040 |
| Highest-revenue menu item | Paneer Tikka |
| Highest-quantity menu item | Gulab Jamun |
| Highest-revenue category | Main Course |

These results describe the included sample data only and should not be interpreted as actual restaurant business performance.

## Documentation

- [Data Dictionary](docs/data_dictionary.md)
- [Test Cases](docs/test_cases.md)

## Limitations

- The project currently uses a small sample dataset.
- The analysis is performed through a command-line application.
- Charts are saved as image files rather than displayed in an interactive dashboard.
- The findings may not represent real-world restaurant sales.

## Future Improvements

- Build an interactive dashboard using Streamlit.
- Add more restaurant sales records.
- Introduce date-range and category filters.
- Add additional business KPIs.
- Improve data validation and automated test coverage.
- Deploy the dashboard for online access.

## Disclaimer

This project is intended for educational and demonstration purposes.

## Author

Project repository maintained by the repository owner.
