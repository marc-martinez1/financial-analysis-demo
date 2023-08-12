# -*- coding: UTF-8 -*-
"""PyRamen Homework Starter."""

# @TODO: Import libraries
import csv
from pathlib import Path

# @TODO: Set file paths for menu_data.csv and sales_data.csv
menu_filepath = Path('Resources/menu_data.csv')
sales_filepath = Path('Resources/sales_data.csv')
file_output = Path('Analysis/ichiban_ramen_report.txt)')

# @TODO: Initialize list objects to hold our menu and sales data
menu = []
sales = []
line_num = 0

# @TODO: Read in the menu data into the menu list
with open(menu_filepath) as menu_data:
    menu_reader = csv.reader(menu_data)
    header = next(menu_reader)
    line_num += 1
    
    for row in menu_reader:
        menu.append(row)

# @TODO: Read in the sales data into the sales list
with open(sales_filepath) as sales_data:
    sales_reader = csv.reader(menu_data)
    header = next(sales_reader)
    line_num += 1
    
    for row in sales_reader:
        sales.append(row)

# @TODO: Initialize dict object to hold our key-value pairs of items and metrics
report = {}

# Initialize a row counter variable
row_count = 0

# @TODO: Loop over every row in the sales list object
for sales_row in sales:
    # Line_Item_ID,Date,Credit_Card_Number,Quantity,Menu_Item
    # @TODO: Initialize sales data variables
    line_item_id = sales_row[0]
    date = sales_row[1]
    credit_card_number = sales_row[2]
    quantity = int(sales_row[3])
    menu_item = sales_row[4]

    # @TODO:
    # If the item value not in the report, add it as a new entry with initialized metrics
    # Naming convention allows the keys to be ordered in logical fashion, count, revenue, cost, profit
    if menu_item not in report.keys():
        report[menu_item] = {
            "01-count": 0,
            "02-revenue": 0,
            "03-cogs": 0,
            "04-profit": 0,
        }
        
    # @TODO: For every row in our sales data, loop over the menu records to determine a match
    for menu_row in menu:
        
        # Item,Category,Description,Price,Cost
        # @TODO: Initialize menu data variables
        item = menu_row[0]
        category = menu_row[1]
        description = menu_row[2]
        price = float(menu_row[3])
        cost = float(menu_row[4])

        # @TODO: Calculate profit of each item in the menu data
        profit = price - cost

        # @TODO: If the item value in our sales data is equal to the any of the items in the menu, then begin tracking metrics for that item
        if (menu_item == item):

            # @TODO: Print out matching menu data
            print(menu_row)

            # @TODO: Cumulatively add up the metrics for each item key
            report[menu_item]["01-count"] += quantity
            report[menu_item]["02-revenue"] += price * quantity
            report[menu_item]["03-cogs"] += cost * quantity
            report[menu_item]["04-profit"] += profit * quantity

        # @TODO: Else, the sales item does not equal any fo the item in the menu data, therefore no match
        else:
            print('The sales item does not equal any of the items in the menu data, therefore no match')

    # @TODO: Increment the row counter by 1
    row_count += 1

# @TODO: Print total number of records in sales data
print(f'Sales data records: {row_count}')

# @TODO: Write out report to a text file (won't appear on the command line output)
with open(file_output, 'w') as output:
    output.write('Ichiban Ramen Report from Jan 01, 2017 to Dec 31, 2018\n')
    for a, b in report.items()
        output.write(f'{a} {b}\n')