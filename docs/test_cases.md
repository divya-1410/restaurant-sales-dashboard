
# Test Cases

## Project: Restaurant Sales Dashboard

### Purpose

This document describes the test scenarios used to check the correctness of the restaurant sales analysis functions.

| Test ID | Test Scenario | Expected Result | Status |
|---|---|---|---|
| TC-01 | Calculate revenue for each sales record | Revenue equals Quantity × Price | Passed — verified |
| TC-02 | Calculate total revenue | Total equals the sum of all record revenues | Passed — verified |
| TC-03 | Calculate revenue by item | Items are grouped and ranked by revenue | Passed — verified |
| TC-04 | Calculate quantity by item | Quantities are grouped and ranked correctly | Passed — verified |
| TC-05 | Load the CSV dataset | Six rows and five columns are loaded | Passed — verified |
| TC-06 | Clean the sample dataset | Six valid rows remain with no missing values or duplicates | Passed — verified |
| TC-07 | Generate revenue chart | Revenue chart image is saved | Passed — verified |
| TC-08 | Generate daily revenue chart | Daily revenue chart image is saved | Passed — verified |

## Notes

- The analysis tests were run using pytest.
- The data loading and cleaning checks were run using Python commands.
- The chart generation checks confirmed that both PNG files were created.
- These results apply to the sample dataset and checks performed so far.
- Additional tests will be added as the project develops.
