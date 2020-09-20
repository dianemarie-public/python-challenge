## PyBank

# Create a Python script that analyzes the records to calculate each of the following:

    # The total number of months included in the dataset
    # The net total amount of "Profit/Losses" over the entire period
    # The average of the changes in "Profit/Losses" over the entire period
    # The greatest increase in profits (date and amount) over the entire period
    # The greatest decrease in losses (date and amount) over the entire period

# In addition, your final script should both print the analysis to the terminal and export a text file with the results.

# Import dependencies for creating file paths across operating systems and reading csv files
import os
import csv

# Set the file path using the os module (imported above), and print
csvfile = os.path.join('Resources', 'budget_data.csv')
print(f"CSV File: {csvfile}")

# Read the file using the csv module, (imported above) Ref: read_csv.py
with open(csvfile) as csvfile:
    # Specifies delimiter and variable that holds contents, and print
    csvreader = csv.reader(csvfile, delimiter=',')
    print(f"CSV Reader: {csvreader}")
    # Read the header row first, and print
    csvheader = next(csvreader)
    print(f"CSV Header: {csvheader}")
    # Read each row after the header row, and print
    for csvrows in csvreader:
        print(csvrows)    