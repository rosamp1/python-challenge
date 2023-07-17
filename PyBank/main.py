# Import budget_data.csv file
import os
import csv

csvpath = os.path.join("Resources","budget_data.csv")

with open(csvpath) as csvfile:
    
    csvreader = csv.reader(csvfile, delimiter=',')

    csv_header = next(csvreader)
    
# The total number of months included in the dataset

    rowcount = 0
    net_total = 0
    previous_profit_loss = 0
    total_changes = 0
    greatest_increase = 0
    greates_incres_month = ""
    greatest_decrease = 0
    greatest_decrease_month = ""

# The net total amount of "Profit/Losses" over the entire period
# The changes in "Profit/Losses" over the entire period, and then the average of those changes
    for row in csvreader:
        rowcount += 1
        current_profit_loss = int(row[1])
        net_total += current_profit_loss

        if rowcount > 1:
            change = current_profit_loss - previous_profit_loss
            total_changes += change

 # The greatest increase in profits (date and amount) over the entire period
            
            if change > greatest_increase:
                greatest_increase = change
                greatest_increase_month = row[0]

# The greatest decrease in profits (date and amount) over the entire period

            if change < greatest_decrease:
                greatest_decrease = change
                greatest_decrease_month = row[0]

        previous_profit_loss = current_profit_loss

    average_change = total_changes/(rowcount-1) if rowcount>1 else 0

# Final script should both print the analysis to the terminal and export a text file with the results


    print(f"Number of months:{rowcount}")
    print(f"Net Total amount of profit/Losses: ${net_total}") 
    print(f"Changes in profit/loss: ${total_changes}")   
    print(f"Average change in profit/loss:{average_change:.2f}")   
    print(f"Greatest increase in profits: {greatest_increase_month} (${greatest_increase})") 
    print(f"Greatest decrease in profits: {greatest_decrease_month} (${greatest_decrease})")










