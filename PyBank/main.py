# Import budget_data.csv file
import os
import csv

csvpath = os.path.join("Resources","budget_data.csv")

with open(csvpath) as csvfile:
    
    csvreader = csv.reader(csvfile, delimiter=',')

    csv_header = next(csvreader)
    
    for row in csvreader:
        print(row)
        






# Create a python script that analyzes the records to calculate each of the foloowing values:
# The toal number of months included in the dataset
# The net total amount of "Profit/Losses" over the entire period
# The changed in "Profit/Losses" over the entire perios, and then the average of thise changes
# The greatest increase in profits (date and amount) over the entire period
# The greatest decrease in profits (date and amount) over the entire period
# Final script should both print the analysis to the terminal and export a text file with the results