## PyBank

# Create a Python script that analyzes the records to calculate each of the following:

    # The total number of months included in the dataset
    # The net total amount of "Profit/Losses" over the entire period
    # The average of the changes in "Profit/Losses" over the entire period
    # The greatest increase in profits (date and amount) over the entire period
    # The greatest decrease in losses (date and amount) over the entire period

# In addition, your final script should both print the analysis to the terminal and export a text file with the results.


import os
import csv

csvpath = os.path.join('Resources', 'budget_data.csv')

file_name = 'budget_data.csv'

with open(csvpath) as csvfile:
  
    csvreader = csv.reader(csvfile, delimiter=',')

    csvheader = next(csvreader)

    total = 0

    budget_amt = [[row[1], int(row[1])] for row in csvreader if row]

    total += (budget_amt[1])

    print(f"Data file: {file_name}")

    for csvrows in budget_amt:
        print(budget_amt)
        print(total)
