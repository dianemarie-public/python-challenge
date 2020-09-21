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

    budget_reader = csv.DictReader(csvfile) # Initiates DictReader from the csv module (ref: Python Documentation here https://docs.python.org/3/library/csv.html#module-contents)
    next(budget_reader) # Skips over header row
    
    net_budget = 0
    avg_budget = 0
    max_profit = 0
    max_loss = 0
    
    budget_month = {} # Dictionary name for 'Date'
    profit_loss = {} # Dictionary name for 'Profit/Losses'
    
    for row in budget_reader: # Reads each row of the dictionary
       budget_line = row['Profit/Losses']       
       if budget_line in profit_loss:           
           budget_line = [int(i) for i in row[1:]] # Converts dictionary list of values to integers Ref: https://stackoverflow.com/questions/38640365/how-do-i-convert-dictionary-list-values-to-integers      
                 
    budget_months = budget_reader.line_num - 1 # Creates variable for counting the number of lines, minus the header row  

print(f"Budget File: {budget_file}") # Prints read file name
print(f"Analysis File: {output_path}") # Prints write file name
print(f"Number of Budget Months: {budget_months}") # Prints the variable value
print(f"Last Budget Line Converted to Integers: {budget_line}")
print(f"Net Profit/Losses: {net_budget}") # Prints the variable value
print(f"Average Profit/Losses: {avg_budget}") # Prints the variable value
print(f"Greatest Increase Profit/Losses: {max_profit}") # Prints the variable value
print(f"Greatest Decrease Profit/Losses: {max_loss}") # Prints the variable value
print(f"Field Names: {budget_reader.fieldnames}") # Prints field names (i.e. header row)

with open(output_path, "w", newline='') as csvfile: # Opens output file, and writes to it (ref: Python Documentation here https://docs.python.org/3/library/csv.html)
    outputwriter = csv.writer(csvfile, delimiter=' ', quotechar=' ', quoting=csv.QUOTE_MINIMAL)
    outputwriter.writerow(['Number of budget months: ', budget_months]) # WORKS
    outputwriter.writerow(['Net profit/losses: ', net_budget])
    outputwriter.writerow(['Average profit/losses: ', avg_budget])
    outputwriter.writerow(['Greatest increase profit/losses: ', max_profit])
    outputwriter.writerow(['Greatest decrease profit/losses: ', max_loss])