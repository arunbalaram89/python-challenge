import os
import csv
import math

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



print("Election Results")
print ("------------------------------------")
print("Total Votes: {ttl_votes}")
print("-------------------------------------")
print("Charles Casper Stockham: {Charles}")
print("Diana DeGette {Diana}")
print("Raymon Anthony Doane {Raymon}")
print("-------------------------------------")
print("Winner: {Winner}")
