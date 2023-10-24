import os
import csv
import math

electionpath = os.path.join('Resources','election_data.csv')

ttl_votes = 0
candidates = {}


# Election Data 


# Read the header row first

with open(electionpath, 'r') as csvfile:
    electionreader = csv.reader(csvfile, delimiter=',')
    election_header = next(electionreader)
    print(f"Election Headers:{election_header}")

    for polling in electionreader:
        # Total Election votes
        ttl_votes += 1
        try: 
            candidates[polling[2]]+=1
        except:
            candidates[polling[2]]=1    


# Zip file in cleaned csv 

#Set variable for the output file
election_output_file = os.path.join("election_final.txt")
output = "Election Results\n"
output+= "------------------------------------\n"
output+= f"Total Votes: {ttl_votes}\n"
output+= "-------------------------------------\n"
winner = [0, ""]
for name, votes in candidates.items():
    output+=f"{name}: {round(votes/ttl_votes * 100, 2)}% ({votes})\n"
    if votes > winner[0]:
        winner[0] = votes
        winner[1] = name
output+= "-------------------------------------\n"
output+= f"Winner: {winner[1]}"




#  Open the output file
with open(election_output_file, "w") as election_datafile:
   election_datafile.write(output)



print(output)


