import os
import csv
import math

budgetpath = os.path.join('..','Resources','budget_data.csv')



# Method 1: Plain Read of Budget Data CSV file
with open(budgetpath, 'r') as file_handler:
    budgetlines = file_handler.read()
    # print(budgetlines)

## Read the header row first

with open(budgetpath, 'r') as csvfile:
    budgetreader = csv.reader(csvfile, delimiter=',')
    budget_header = next(budgetreader)
    print(f"Budget Headers:{budget_header}")























