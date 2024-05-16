import json
import matplotlib.pyplot as plt
from tkinter import *
from tkinter import messagebox
from datetime import datetime

# Function to add expense
def add_expense():
    date_str = date_entry.get()
    amount = float(amount_entry.get())
    category = category_var.get()
    if category == "Other":
        custom_category = custom_category_entry.get().strip()
        if custom_category:
            category = custom_category
    date = datetime.strptime(date_str, "%d-%m-%Y")
    expenses.append({"date": date.strftime("%d-%m-%Y"), "amount": amount, "category": category})
    save_expenses()
    messagebox.showinfo("Expense Added", "Expense added successfully.")

# Function to save expenses to JSON file
def save_expenses():
    with open('expenses.json', 'w') as f:
        json.dump(expenses, f)

# Function to plot spending graph
def plot_spending():
    start_date_str = start_date_entry.get()
    end_date_str = end_date_entry.get()
    start_date = datetime.strptime(start_date_str, "%d-%m-%Y").strftime("%d-%m-%Y")
    end_date = datetime.strptime(end_date_str, "%d-%m-%Y").strftime("%d-%m-%Y")
    
    filtered_expenses = [expense for expense in expenses if start_date <= expense["date"] <= end_date]
    dates = [expense["date"] for expense in filtered_expenses]
    amounts = [expense["amount"] for expense in filtered_expenses]

    plt.plot(dates, amounts, marker='o')
    plt.xlabel('Date')
    plt.ylabel('Amount')
    plt.title('Spending Over Time')
    plt.xticks(rotation=45)
    plt.tight_layout()
    plt.show()

# Load expenses from JSON file
try:
    with open('expenses.json', 'r') as f:
        expenses = json.load(f)
except FileNotFoundError:
    expenses = []

# Create main window
root = Tk()
root.title("Expense Tracker")

# Add expense section
add_frame = LabelFrame(root, text="Add Expense")
add_frame.pack(padx=10, pady=10)

date_label = Label(add_frame, text="Date (dd-mm-yyyy):")
date_label.grid(row=0, column=0, padx=5, pady=5)
date_entry = Entry(add_frame)
date_entry.grid(row=0, column=1, padx=5, pady=5)

amount_label = Label(add_frame, text="Amount:")
amount_label.grid(row=1, column=0, padx=5, pady=5)
amount_entry = Entry(add_frame)
amount_entry.grid(row=1, column=1, padx=5, pady=5)

category_label = Label(add_frame, text="Category:")
category_label.grid(row=2, column=0, padx=5, pady=5)
categories = ["Food", "Clothes", "Groceries", "Other"]
category_var = StringVar()
category_var.set(categories[0])
category_dropdown = OptionMenu(add_frame, category_var, *categories)
category_dropdown.grid(row=2, column=1, padx=5, pady=5)

custom_category_label = Label(add_frame, text="Custom Category:")
custom_category_label.grid(row=3, column=0, padx=5, pady=5)
custom_category_entry = Entry(add_frame)
custom_category_entry.grid(row=3, column=1, padx=5, pady=5)
custom_category_entry.config(state=DISABLED)

def toggle_custom_category(*args):
    if category_var.get() == "Other":
        custom_category_entry.config(state=NORMAL)
    else:
        custom_category_entry.config(state=DISABLED)

category_var.trace("w", toggle_custom_category)

add_button = Button(add_frame, text="Add Expense", command=add_expense)
add_button.grid(row=4, columnspan=2, padx=5, pady=5)

# Plot spending section
plot_frame = LabelFrame(root, text="Plot Spending")
plot_frame.pack(padx=10, pady=10)

start_date_label = Label(plot_frame, text="Start Date (dd-mm-yyyy):")
start_date_label.grid(row=0, column=0, padx=5, pady=5)
start_date_entry = Entry(plot_frame)
start_date_entry.grid(row=0, column=1, padx=5, pady=5)

end_date_label = Label(plot_frame, text="End Date (dd-mm-yyyy):")
end_date_label.grid(row=1, column=0, padx=5, pady=5)
end_date_entry = Entry(plot_frame)
end_date_entry.grid(row=1, column=1, padx=5, pady=5)

plot_button = Button(plot_frame, text="Plot Spending", command=plot_spending)
plot_button.grid(row=2, columnspan=2, padx=5, pady=5)

root.mainloop()
