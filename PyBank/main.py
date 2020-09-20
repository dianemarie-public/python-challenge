## PyBank

# Create a Python script that analyzes the records to calculate each of the following:

    # The total number of months included in the dataset
    # The net total amount of "Profit/Losses" over the entire period
    # The average of the changes in "Profit/Losses" over the entire period
    # The greatest increase in profits (date and amount) over the entire period
    # The greatest decrease in losses (date and amount) over the entire period

# In addition, your final script should both print the analysis to the terminal and export a text file with the results.

# Import dependencies for creating file paths across operating systems and reading csv files Ref: imports.py
import os
import csv

# Set the file path using the os module (imported above), and print
csvfile = os.path.join('Resources', 'budget_data.csv')
print(f"CSV File: {csvfile}")

output_path = os.path.join("Analysis", "output.txt")
print(f"Analysis File: {output_path}")

# Open and read csv file using the csv module, (imported above) Ref: examples read_csv.py, cereal_solved.py
with open(csvfile) as csvfile:
    # Using DictReader from the csv module, creates an object that maps each row to a dictionary where keys are given fieldnames, defaulted to the first header row (ref: Python Documentation for csv module here https://docs.python.org/3/library/csv.html#module-contents)
    dict_reader = csv.DictReader(csvfile)    
    # Prints field names (i.e. header row)
    print(f"Field Names: {dict_reader.fieldnames}")
    # Read and print each row as dictionary
    for rows in dict_reader:
        next(dict_reader)
        print(rows)
    # Print the number of rows, minus the header row
    budget_months = dict_reader.line_num - 1
    print(f"Number of Budget Months: {budget_months}")
with open(output_path, "w", newline='') as csvfile:
    outputwriter = csv.writer(csvfile, delimiter=' ', quotechar=' ', quoting=csv.QUOTE_MINIMAL)
    outputwriter.writerow(['Number of budget months: '])
    outputwriter.writerow(['Net profit/losses: '])
    outputwriter.writerow(['Average profit/losses: '])
    outputwriter.writerow(['Greatest increase profit/losses: '])
    outputwriter.writerow(['Greatest decrease profit/losses: '])
    outputwriter.writerow(['Net profit/losses: '])

    ############ WORKS ABOVE THIS LINE ########