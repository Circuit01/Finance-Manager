# Finance-Manager
This Python finance manager (work in progress) tracks and visualises your expenses. With Tkinter and Matplotlib, users can add expenses, categorise them, and plot spending. Data is saved in a JSON file.

## Overview
This Expense Tracker is a simple Python application that allows you to track and visualise your expenses over time. It provides a user-friendly interface to add expenses, save them to a JSON file, and plot spending data using a graph.

## Features
- Add expenses with date, amount, and category.
- Save expenses to a JSON file.
- Plot spending over a specified date range.

## Requirements
- Python 3.x
- `matplotlib` library
- `tkinter` library (comes with standard Python installation)

## Installation
1. Ensure you have Python 3.x installed on your system.
2. Install the `matplotlib` library if you don't already have it:
   ```sh
   pip install matplotlib
   ```

## How to Use
1. **Run the Application**: Execute the script to open the Expense Tracker GUI.
   ```sh
   python expense_tracker.py
   ```
2. **Add an Expense**:
   - Enter the date in `dd-mm-yyyy` format.
   - Enter the amount spent.
   - Select a category from the dropdown menu or enter a custom category if "Other" is selected.
   - Click "Add Expense" to save the expense.
3. **Plot Spending**:
   - Enter the start date and end date in `dd-mm-yyyy` format.
   - Click "Plot Spending" to view a graph of your expenses over the selected date range.

## Code Explanation

### Importing Libraries
```python
import json
import matplotlib.pyplot as plt
from tkinter import *
from tkinter import messagebox
from datetime import datetime
```
- `json`: For saving and loading expenses.
- `matplotlib.pyplot`: For plotting spending graphs.
- `tkinter`: For creating the graphical user interface.
- `datetime`: For handling date formats.

### Functions
- **`add_expense`**: Adds a new expense entry to the list and saves it to the JSON file.
- **`save_expenses`**: Saves the list of expenses to a JSON file.
- **`plot_spending`**: Plots a graph of expenses over a specified date range.

### GUI Setup
- **Main Window**: Created using `Tk()`.
- **Add Expense Section**: Includes input fields for date, amount, category, and a button to add the expense.
- **Plot Spending Section**: Includes input fields for start and end dates and a button to plot the spending graph.

## Example
1. Open the application.
2. Add an expense for `01-01-2023`, amount `50.0`, category `Food`.
3. Add another expense for `02-01-2023`, amount `30.0`, category `Groceries`.
4. Enter the start date `01-01-2023` and end date `02-01-2023` and click "Plot Spending" to see a graph of these expenses.

## Files
- **`expense_tracker.py`**: Main script file.
- **`expenses.json`**: File where expenses are saved.

## Troubleshooting
- Ensure the date format is correct (`dd-mm-yyyy`).
- Ensure `matplotlib` is installed properly.
- If the JSON file is corrupted or missing, the script will create a new one.

## Conclusion
This Expense Tracker is a simple yet effective way to keep track of your spending and visualise it over time. Customise it further as needed to suit your personal or professional needs.
