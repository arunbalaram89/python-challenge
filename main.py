import os
import csv
import math



budgetpath = os.path.join('..','Resources','budget_data.csv')


ttl_months = []
net_profit = []
avg_change = []
greatest_increase_profits = []
greatest_decrease_profits = []

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
   
    for column in budgetreader:
        header = next(budgetreader)
        # Add Total Months
        ttl_months.append(column[0])
        # Add Net Profit
        net_profit.append(column[1])
        # Get the average change 
        first_row = budgetreader
         
        # Determine changes of Profit/Loss and then average of changes
        prev_net = int(first_row[1])
        net_change = int(first_row[1]) - prev_net
        net_change_list += [net_change]
        avg_change = sum(net_change_list) / len(net_change_list)
        avg_change.append(column[1])
    
        # Determine greatest increase in Profits (Date and Amount) over the entire period
        greatest_increase_profits.append(int+=(column[1]))
        # Determine greatest decrease in profits (Date and Amount) over the entire period

        greatest_decrease_profits.append(int-=(column[1]))




# Zip file in cleaned csv 
cleaned_budget_csv = zip(ttl_months, net_profit, avg_change, greatest_increase_profits, greatest_decrease_profits)

#Set variable for the output file
budget_output_file = os.path.join("budget_final.txt")


#  Open the output file
with open(budget_output_file, "w") as budget_datafile:
    budgetwriter = csv.writer(budget_datafile)

    # Write the header row
    budgetwriter.writerow(["Total Months", "Net Profits" , "Average Change", "Greatest Increase in Profit", "Greatest Decrease in Profit"])

    # Write in zipped rows
    budgetwriter.writerows(cleaned_budget_csv.txt)










electionpath = os.path.join('..','Resources','election_data.csv')

ttl_votes = []
Charles = []
Diana = []
Raymon = []    
Winner = []

# Election Data 

with open(electionpath, 'r') as file_handler:
    electionlines = file_handler.read()
    print(electionlines)

# Read the header row first

with open(electionpath, 'r') as csvfile:
    electionreader = csv.reader(csvfile, delimiter=',')
    election_header = next(electionreader)
    print(f"Election Headers:{election_header}")

   


    for polling in electionreader:
        election_header = next(electionreader)
        # Total Election votes
        ttl_votes.append(polling[0])
        # Diana's Election result 
        diana_voting = candidate1 == "Diana DeGette",
        Diana.append(polling[2])
        # Charles Casper Stockham
        charles_voting = candidate2 == "Charles Casper Stockham"
        Charles.append(polling[2])
        # Raymon Anthony Doane
        raymon_voting = candidate3 == "Raymon Anthony Doane"
        Raymon.append(polling[2])
        #Winner 
        winner_voting = electioncount
        Winner.append(polling[2])


# Zip file in cleaned csv 
cleaned_election_csv = zip(ttl_votes, Charles, Diana, Raymon, Winner)

#Set variable for the output file
election_output_file = os.path.join("election_final.txt")


#  Open the output file
with open(election_output_file, "w") as election_datafile:
    election_write = csv.writer(election_datafile)

    # Write the header row
    election_write.writerow(["Election Results"])

    # Write in zipped rows
    election_write.writerows(election_datafile.txt)









print("BUDGET DATA")
print("-------------------------------------")
print(f"Total number of months in the budget data is: {ttl_months}")
print(f"The total net total amount of Profit and Losses over the entire period is{net_profit}")
print(f"The changes in Profit/Losses over the entire period, and then the average of those changes{avg_change}")
print(f"The greatest increase in profits (date and amount) over the entire period{greatest_increase_profits}")
print(f"The greatest decrease in profits (date and amount) over the entire period{greatest_decrease_profits}")




print("Election Results")
print ("------------------------------------")
print("Total Votes: {ttl_votes}")
print("-------------------------------------")
print("Charles Casper Stockham: {Charles}")
print("Diana DeGette {Diana}")
print("Raymon Anthony Doane {Raymon}")
print("-------------------------------------")
print("Winner: {Winner}")
















