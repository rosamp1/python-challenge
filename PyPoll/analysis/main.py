# Import budget_data.csv file
import os
import csv


csvpath = os.path.join("Resources","election_data.csv")

with open(csvpath) as csvfile:
    
    csvreader = csv.reader(csvfile, delimiter=',')
    csv_header = next(csvreader)
    print(csvreader)

    for row in csvreader:
        print(row)
