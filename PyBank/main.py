## PyBank

# Create a Python script that analyzes the records to calculate each of the following:

import os 
import csv 
# Imports the dependencies to: create file paths across operating systems (os) and read from csv files (csv)

csv_path = os.path.join('Resources', 'budget_data.csv') 
text_path = os.path.join("Analysis", "output.txt") 
# Set the csv (read from) and text (write to) file paths using the os module (imported above)
file_name = 'budget_data.csv'
# Creates variables, and set initial values to zero (as integers)
num_months = 0 # The total number of months included in the dataset
net_profit_loss = 0 # The net total amount of "Profit/Losses" over the entire period
avg_profit_loss = 0 # The average of the changes in "Profit/Losses" over the entire period
max_profit = 0 # The greatest increase in profits (date and amount) over the entire period
max_loss = 0 # The greatest decrease in losses (date and amount) over the entire period

with open(csv_path, 'r') as csvfile: # Opens and reads the file using the csv module
    csv_reader = csv.DictReader(csvfile) # Initiates DictReader from csv module, and the ability to reference dictionary keys (i.e. "Profit/Losses")
    for row in csv_reader: # Reads each row of the dictionary
        budget_row = int(row["Profit/Losses"]) # Converts content of column to integer, example here: https://courses.cs.washington.edu/courses/cse140/13wi/csv-parsing.html
        net_profit_loss += int(row["Profit/Losses"])
        if max_profit == 0 or max_profit < budget_row: # If statement example for largest value found here: https://courses.cs.washington.edu/courses/cse140/13wi/csv-parsing.html
            max_profit = int(budget_row)
        if max_loss == 0 or max_loss > budget_row: # If statement example (above) reversed for smallest value
            max_loss = int(budget_row)   
    num_months = csv_reader.line_num - 1 # Creates variable for counting the number of lines, minus the header row     
    avg_profit_loss = "${:,.2f}".format(net_profit_loss/num_months) # Formats the variable with two decimal points, comma separators and a preceeding dollar sign
    net_profit_loss = "${:,.2f}".format(net_profit_loss) # Formats the variable with two decimal points, comma separators and a preceeding dollar sign
    max_profit = "${:,.2f}".format(max_profit) # Formats the variable with two decimal points, comma separators and a preceeding dollar sign
    max_loss = "${:,.2f}".format(max_loss) # Formats the variable with two decimal points, comma separators and a preceeding dollar sign
    # Formatting with comma separators: https://www.kite.com/python/answers/how-to-add-commas-to-a-number-in-python
    # Formatting with two decimal points: https://www.kite.com/python/answers/how-to-print-a-float-with-two-decimal-places-in-python#:~:text=Use%20str.,float%20with%20two%20decimal%20places&text=format(number)%20with%20%22%7B,string%20to%20print%20the%20float.
    # Formatting with leading dollar sign:  https://www.daniweb.com/programming/software-development/threads/463071/percentages-and-dollar-signs-in-output 
    
    print(f"CSV Path: {csv_path}") # Prints to terminal
    print(f"Analysis Path: {text_path}") # Prints to terminal
    print(f" ") # Prints to terminal
    print(f"Budget Analysis of {file_name}") # Prints to terminal
    print(f"Number of Months: {num_months}") # Prints to terminal
    print(f"Net Profit/Loss: {net_profit_loss}") # Prints to terminal
    print(f"Average Profit/Loss: {avg_profit_loss}") # Prints to terminal
    print(f"Greatest Increase Profit/Loss: {max_profit}") # Prints to terminal
    print(f"Greatest Decrease Profit/Loss: {max_loss}") # Prints to terminal

# Opens output file, and writes to it (ref: Python Documentation here https://docs.python.org/3/library/csv.html#writer-objects
with open(text_path, "w", newline='') as csvfile: # Eliminate blank lines in output: https://stackoverflow.com/questions/3348460/csv-file-written-with-python-has-blank-lines-between-each-row
    text_writer = csv.writer(csvfile, delimiter=' ', quotechar=' ', quoting=csv.QUOTE_MINIMAL) # Used example included in csv.writer (i.e. spamwriter): https://docs.python.org/3/library/csv.html
    text_writer.writerow(['Budget Analysis of',file_name]) # Prints to the output.txt file
    text_writer.writerow(['Number of Months:',num_months]) # Prints to the output.txt file
    text_writer.writerow(['Net Profit/Loss:',net_profit_loss]) # Prints to the output.txt file
    text_writer.writerow(['Average Profit/Losses:',avg_profit_loss]) # Prints to the output.txt file
    text_writer.writerow(['Greatest Increase Profit/Loss:',max_profit]) # Prints to the output.txt file
    text_writer.writerow(['Greatest Decrease Profit/Loss:',max_loss]) # Prints to the output.txt file