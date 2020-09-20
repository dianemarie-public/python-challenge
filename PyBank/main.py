## PyBank

# Create a Python script that analyzes the records to calculate each of the following:

    # The total number of months included in the dataset
    # The net total amount of "Profit/Losses" over the entire period
    # The average of the changes in "Profit/Losses" over the entire period
    # The greatest increase in profits (date and amount) over the entire period
    # The greatest decrease in losses (date and amount) over the entire period

# In addition, your final script should both print the analysis to the terminal and export a text file with the results.

import os # Imports the dependency for creating file paths across operating systems
import csv # Imports the dependency for reading csv files Ref: imports.py

budget_file = os.path.join('Resources', 'budget_data.csv') # Set the file path using the os module (imported above)
output_path = os.path.join("Analysis", "output.txt")

with open(budget_file, 'r') as csvfile: # Opens and reads the file using the csv module (imported above) Ref: examples read_csv.py, cereal_solved.py

    budget_reader = csv.DictReader(csvfile) # Initiates DictReader from the csv module to create an object that maps each row to a dictionary, where keys are given fieldnames, defaulted to the first header row (ref: Python Documentation for csv module here https://docs.python.org/3/library/csv.html#module-contents)

    for rows in budget_reader: # Reads each row of the dictionary
        next(budget_reader) # Reads the next row
        
        # print(sum(net_budget.values())) # Ref: https://stackoverflow.com/questions/4880960/how-to-sum-all-the-values-in-a-dictionary
    net_budget = 0
    budget_months = budget_reader.line_num - 1 # Creates variable for counting the number of lines, minus the header row  

print(f"Budget File: {budget_file}") # Prints read file name
print(f"Analysis File: {output_path}") # Prints write file name
print(f"Field Names: {budget_reader.fieldnames}") # Prints field names (i.e. header row)
print(f"Number of Budget Months: {budget_months}") # Prints the variable value
print(f"Net Profit/Losses: {net_budget}") # Prints the variable value

# Open output file and write to it (ref: Python Documentation for csv.writer here https://docs.python.org/3/library/csv.html)
with open(output_path, "w", newline='') as csvfile:
    outputwriter = csv.writer(csvfile, delimiter=' ', quotechar=' ', quoting=csv.QUOTE_MINIMAL)
    outputwriter.writerow(['Number of budget months: ', budget_months]) # WORKS
        ############ WORKS ABOVE THIS LINE ########
    outputwriter.writerow(['Net profit/losses: ', net_budget])
    outputwriter.writerow(['Average profit/losses: '])
    outputwriter.writerow(['Greatest increase profit/losses: '])
    outputwriter.writerow(['Greatest decrease profit/losses: '])
    outputwriter.writerow(['Net profit/losses: '])

