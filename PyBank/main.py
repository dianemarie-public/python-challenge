## PyBank

# Create a Python script that analyzes the records to calculate each of the following:

    # The total number of months included in the dataset
    # The net total amount of "Profit/Losses" over the entire period
    # The average of the changes in "Profit/Losses" over the entire period
    # The greatest increase in profits (date and amount) over the entire period
    # The greatest decrease in losses (date and amount) over the entire period

import os 
import csv 
# Imports the dependencies to: create file paths across operating systems (os) and read from csv files (csv)

csv_path = os.path.join('Resources', 'budget_data.csv') 
text_path = os.path.join("Analysis", "output.txt") 
# Set the csv (read from) and text (write to) file paths using the os module (imported above)

# Creates variables, and set initial vale to zero (integers)
num_months = 0
net_profit_loss = 0
avg_profit_loss = 0
max_profit = 0
max_loss = 0

with open(csv_path, 'r') as csvfile: # Opens and reads the file using the csv module
    csv_reader = csv.DictReader(csvfile) # Initiates DictReader from csv module
    print(f"CSV Reader: {csv_reader}")
    
    for row in csv_reader: # Reads each row of the dictionary
       budget_row = int(row["Profit/Losses"]) # Converts content of column to integer, example here: https://courses.cs.washington.edu/courses/cse140/13wi/csv-parsing.html  
       
       if budget_line in profit_loss:           
           budget_line = [int(i) for i in row[1:]] 
    budget_months = budget_reader.line_num - 1 # Creates variable for counting the number of lines, minus the header row  

# Prints analysis to terminal
print(f"Budget Analysis")
print(f"Number of Budget Months: {budget_months}") 
print(f"Last Budget Line Converted to Integers: {budget_line}")
print(f"Net Profit/Losses: {net_budget}") 
print(f"Average Profit/Losses: {avg_budget}") 
print(f"Greatest Increase Profit/Losses: {max_profit}") 
print(f"Greatest Decrease Profit/Losses: {max_loss}") 
print(f"Field Names: {budget_reader.fieldnames}") 

# Prints analysis to the output.txt file
with open(output_path, "w", newline='') as csvfile: # Opens output file, and writes to it (ref: Python Documentation here https://docs.python.org/3/library/csv.html#writer-objects
    outputwriter = csv.writer(csvfile, delimiter=' ', quotechar=' ', quoting=csv.QUOTE_MINIMAL)
    outputwriter.writerow(['Number of budget months: ', budget_months]) # WORKS
    outputwriter.writerow(['Net profit/losses: ', net_budget])
    outputwriter.writerow(['Average profit/losses: ', avg_budget])
    outputwriter.writerow(['Greatest increase profit/losses: ', max_profit])
    outputwriter.writerow(['Greatest decrease profit/losses: ', max_loss])