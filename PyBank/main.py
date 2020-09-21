## PyBank

# Create a Python script that analyzes the records to calculate each of the following:

# Imports the dependencies to: create file paths across operating systems (os) and read from csv files (csv)
import os 
import csv 

# Set the csv (read from) and text (write to) file paths using the os module (imported above)
csv_path = os.path.join('Resources', 'budget_data.csv') 
text_path = os.path.join("Analysis", "output.txt") 

file_name = 'budget_data.csv'

# Creates variables, and set initial values to zero (as integers), important to set variables before open/read or open/write
num_months = 0 # The total number of months included in the dataset
net_profit_loss = 0 # The net total amount of "Profit/Losses" over the entire period
avg_profit_loss = 0 # The average of the changes in "Profit/Losses" over the entire period
max_profit = 0 # The greatest increase in profits (date and amount) over the entire period
max_loss = 0 # The greatest decrease in losses (date and amount) over the entire period

# Opens and reads the file using the csv module
with open(csv_path, 'r') as csvfile:
    # Initiates DictReader from csv module, and the ability to reference dictionary keys (i.e. "Profit/Losses")
    csv_reader = csv.DictReader(csvfile)
    # Reads each row of the dictionary
    for row in csv_reader:
        # Converts content of column to integer, example here: https://courses.cs.washington.edu/courses/cse140/13wi/csv-parsing.html
        budget_row = int(row["Profit/Losses"]) 
        net_profit_loss += int(row["Profit/Losses"])
        # If statement to compare each row until the largest numeric value is found, example for largest value found here: https://courses.cs.washington.edu/courses/cse140/13wi/csv-parsing.html
        if max_profit == 0 or max_profit < budget_row:
            max_profit = int(budget_row)
        # If statement to compare each row until the smallest numeric value is found, example (above) reversed for smallest value
        if max_loss == 0 or max_loss > budget_row:
            max_loss = int(budget_row)   
    
    # Creates variable for counting the number of lines, minus the header row   
    num_months = csv_reader.line_num - 1
    
    # Format the calculated values after loop, but before print
    avg_profit_loss = "${:,.2f}".format(net_profit_loss/num_months)
    net_profit_loss = "${:,.2f}".format(net_profit_loss)
    max_profit = "${:,.2f}".format(max_profit)
    max_loss = "${:,.2f}".format(max_loss)
    # Formatting with comma separators: https://www.kite.com/python/answers/how-to-add-commas-to-a-number-in-python
    # Formatting with two decimal points: https://www.kite.com/python/answers/how-to-print-a-float-with-two-decimal-places-in-python#:~:text=Use%20str.,float%20with%20two%20decimal%20places&text=format(number)%20with%20%22%7B,string%20to%20print%20the%20float.
    # Formatting with leading dollar sign:  https://www.daniweb.com/programming/software-development/threads/463071/percentages-and-dollar-signs-in-output 
    
    # Prints to terminal
    print(f"CSV Path: {csv_path}") 
    print(f"Analysis Path: {text_path}")
    print(f" ")
    print(f"Budget Analysis of {file_name}")
    print(f"Number of Months: {num_months}")
    print(f"Net Profit/Loss: {net_profit_loss}")
    print(f"Average Profit/Loss: {avg_profit_loss}")
    print(f"Greatest Increase Profit/Loss: {max_profit}")
    print(f"Greatest Decrease Profit/Loss: {max_loss}")

# Opens output file, and writes to it (ref: Python Documentation here https://docs.python.org/3/library/csv.html#writer-objects
with open(text_path, "w", newline='') as csvfile: # Eliminate blank lines in output: https://stackoverflow.com/questions/3348460/csv-file-written-with-python-has-blank-lines-between-each-row
    # Used example included in csv.writer (i.e. spamwriter): https://docs.python.org/3/library/csv.html
    text_writer = csv.writer(csvfile, delimiter=' ', quotechar=' ', quoting=csv.QUOTE_MINIMAL)
    
    # Prints to the output.txt file
    text_writer.writerow(['Budget Analysis of',file_name]) 
    text_writer.writerow(['Number of Months:',num_months])
    text_writer.writerow(['Net Profit/Loss:',net_profit_loss])
    text_writer.writerow(['Average Profit/Losses:',avg_profit_loss])
    text_writer.writerow(['Greatest Increase Profit/Loss:',max_profit])
    text_writer.writerow(['Greatest Decrease Profit/Loss:',max_loss])