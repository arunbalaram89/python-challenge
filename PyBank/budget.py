import os
import csv
import math

budgetpath = os.path.join('Resources','budget_data.csv')


ttl_months = []
net_profit = []
avg_change = []
greatest_increase_profits = [-100000000, ""]
greatest_decrease_profits = [100000000, ""]
prev_net = 0

# Method 1: Plain Read of Budget Data CSV file

with open(budgetpath, 'r') as budget_handler:
    budgetlines = budget_handler.read()
    print(budgetlines)

# Reading in the file using csv reader 

# Read the header row first
# budget_header = next(budgetreader)
# print(f"Budget Headers:{budget_header}")

with open(budgetpath, 'r') as csvfile:
    budgetreader = csv.reader(csvfile, delimiter=',')
    header = next(budgetreader)

    for i,column in enumerate (budgetreader):
        # Add Total Months
        ttl_months.append(column[0])
        # Add Net Profit
        net_profit.append(int(column[1]))
        if i > 0:
        # Get the average change 
        # Determine changes of Profit/Loss and then average of changes
        
            
            net_change = int(column[1]) - prev_net
            avg_change.append(net_change)
            if net_change > greatest_increase_profits[0]:
                greatest_increase_profits[0] = net_change
                greatest_increase_profits[1] = column[0]

            if net_change < greatest_decrease_profits[0]:
                greatest_decrease_profits[0] = net_change
                greatest_decrease_profits[1] = column[0]
        prev_net = int(column[1])       

        # Determine greatest increase in Profits (Date and Amount) over the entire period
        # High_profit += greatest_increase_profits
        # greatest_increase_profits.append(int+=(column[1]))
        # # Determine greatest decrease in profits (Date and Amount) over the entire period
        # Lowest_profit -= greatest_decrease_profits
        # greatest_decrease_profits.append(int-=(column[1]))




# Zip file in cleaned csv 
# cleaned_budget_csv = zip(ttl_months, net_profit, avg_change, greatest_increase_profits, greatest_decrease_profits)

#Set variable for the output file
budget_output_file = os.path.join("budget_final.txt")
output = "BUDGET DATA\n"
output+= "-------------------------------------\n"
output+= f"Total number of months in the budget data is: {len(ttl_months)}\n"
output+= f"The total net total amount of Profit and Losses over the entire period is ${sum(net_profit)}\n"
output+= f"The changes in Profit/Losses over the entire period, and then the average of those changes ${round(sum(avg_change)/len(avg_change), 2)}\n"
output+= f"The greatest increase in profits (date and amount) over the entire period {greatest_increase_profits[1]} ${greatest_increase_profits[0]}\n"
output+= f"The greatest decrease in profits (date and amount) over the entire period {greatest_decrease_profits[1]} ${greatest_decrease_profits[0]}"


#  Open the output file
with open(budget_output_file, "w") as budget_datafile:
    # budgetwriter = csv.writer(budget_datafile)
    budget_datafile.write(output)

    # Write the header row
    # budgetwriter.writerow(["Total Months", "Net Profits" , "Average Change", "Greatest Increase in Profit", "Greatest Decrease in Profit"])

    # Write in zipped rows
    # budgetwriter.writerows(cleaned_budget_csv.txt)



print(output)


