# Import budget_data.csv file
import os
import csv


csvpath = os.path.join("Resources","election_data.csv")

with open(csvpath) as csvfile:
    
    csvreader = csv.reader(csvfile, delimiter=',')
    csv_header = next(csvreader)
    print(csv_header)

    for row in csvreader:
        print(row)



# The total number of votes cast
# A complete list of candidates who received votes
# The percentage of votes each candidate won
# The total number of votes each candidate won
# The winner of the election based on popular vote

