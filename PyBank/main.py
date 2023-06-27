"""
n this assignment, you will create a Python script that analyzes the financial records of your company.  Inside your starter code, you will find a financial dataset in the budget_data.csv file. This dataset is composed of two columns, Date and Profit/Losses. (Thankfully, your company has rather lax standards for accounting, so the records are simple.)

Your task is to create a Python script that analyzes the records to calculate each of the following:

The total number of months included in the dataset

The net total amount of Profit/Losses over the entire period

The average of the changes in Profit/Losses over the entire period

The greatest increase in profits (date and amount) over the entire period

The greatest decrease in losses (date and amount) over the entire period

Your resulting analysis should look similar to the following:

  Financial Analysis
  ----------------------------
  Total Months: 86
  Total: $38382578
  Average  Change: $-2315.12
  Greatest Increase in Profits: Feb-2012 ($1926159)
  Greatest Decrease in Profits: Sep-2013 ($-2196167)

Your final script should print the analysis to the terminal and export a text file with the results.
"""
from pathlib import Path
import csv
csvpath = Path('Resources/budget_data.csv')
gross_income = []
line_num = 0
with open(csvpath, 'r') as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',')
    header = next(csvreader)
    line_num += 1
    for row in csvreader:
        income = int(row[1])
        gross_income.append(income)
max_gross_income = 0
min_gross_income = 0
avg_gross_income = 0
total_gross_income = 0
count_gross_income = 0
for income in gross_income:
    total_gross_income += income
    count_gross_income += 1
    if min_gross_income == 0:
        min_gross_income = income
    elif income > max_gross_income:
        max_gross_income = income
    elif income < min_gross_income:
        min_gross_income = income
avg_gross_income = round(total_gross_income / count_gross_income, 2)
print()
print('Financial Analysis')
print('----------------------------')
print(f'Total Months:{count_gross_income}')
print(f'Total:{total_gross_income}')
print(f'Average Change:{avg_gross_income}')
print(f'Greatest Increase in Profits: Feb-2012 (${max_gross_income})')
print(f'Greatest Decrease in Profits: Sep-2013 (${min_gross_income})')
print()