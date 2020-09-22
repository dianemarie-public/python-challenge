#   * A complete list of candidates who received votes
#   * The percentage of votes each candidate won
#   * The total number of votes each candidate won
#   * The winner of the election based on popular vote.

import os
import csv
import collections 

csv_path = os.path.join('Resources', 'election_data.csv')
text_path = os.path.join("Analysis", "election_results.txt")

csv_file_name = 'election_data.csv'
txt_file_name = 'election_reslts.txt'

voters = collections.Counter()
candidate1_votes = 0
candidate2_votes = 0
candidate3_votes = 0
candidate4_votes = 0
total_votes = 0
winner = 'none'

with open(csv_path, 'r') as csvfile:
    csv_reader = csv.DictReader(csvfile)
    for votes in csv_reader:

        # Counts the number of votes for each candidate                
        if votes['Candidate'] == 'Khan': # Using DictReader the key is the column name, then searches for 'word'
            candidate1_votes += 1 # Totals the number of times 'word' is found in column 'Candidate    
        if votes['Candidate'] == 'Correy':
            candidate2_votes += 1    
        if votes['Candidate'] == 'Li': 
            candidate3_votes += 1
        if votes['Candidate'] == "O'Tooley":
            candidate4_votes += 1

        # Compares the number of votes for each candidate
        if candidate1_votes > candidate2_votes and candidate1_votes > candidate3_votes and candidate1_votes > candidate4_votes:
            winner = "Khan"        
        if candidate2_votes > candidate1_votes and candidate2_votes > candidate3_votes and candidate2_votes > candidate4_votes:
            winner = "Correy"
        if candidate3_votes > candidate1_votes and candidate3_votes > candidate2_votes and candidate3_votes > candidate4_votes:
            winner = "Li"
        if candidate4_votes > candidate1_votes and candidate4_votes > candidate2_votes and candidate4_votes > candidate3_votes:
            winner = "O'Tooley"

    num_lines = csv_reader.line_num - 1
    total_votes = candidate1_votes + candidate2_votes + candidate3_votes + candidate4_votes # Total votes cast
    candidate1_pct = candidate1_votes/total_votes*100
    candidate2_pct = candidate2_votes/total_votes*100
    candidate3_pct = candidate3_votes/total_votes*100
    candidate4_pct = candidate4_votes/total_votes*100
    total_pct = candidate1_pct + candidate2_pct + candidate3_pct + candidate4_pct
   
    # Formats variables before printing
    num_lines = "{:,.0f}".format(num_lines)
    total_votes = "{:,.0f}".format(total_votes)
    candidate1_votes = "{:,.0f}".format(candidate1_votes)
    candidate2_votes = "{:,.0f}".format(candidate2_votes)
    candidate3_votes = "{:,.0f}".format(candidate3_votes)
    candidate4_votes = "{:,.0f}".format(candidate4_votes)
    candidate1_pct = "{:,.0f}%".format(candidate1_pct)
    candidate2_pct = "{:,.0f}%".format(candidate2_pct)
    candidate3_pct = "{:,.0f}%".format(candidate3_pct)
    candidate4_pct = "{:,.0f}%".format(candidate4_pct)
    total_pct = "{:,.0f}%".format(total_pct)   
    
    # Prints to terminal
    print(f"Election Results")
    print(f"Total Votes Cast: {total_votes}, {total_pct}")
    print(f"Votes for Khan: {candidate1_votes}, {candidate1_pct}")
    print(f"Votes for Correy: {candidate2_votes}, {candidate2_pct}")
    print(f"Votes for Li: {candidate3_votes}, {candidate3_pct}")
    print(f"Votes for O'Tooley: {candidate4_votes}, {candidate4_pct}")
    print(f"Election Winner: {winner}")    

with open (text_path, "w", newline='') as csvfile:
    text_writer = csv.writer(csvfile, delimiter=' ', quotechar=' ', quoting=csv.QUOTE_MINIMAL)

    # Prints to election_results.txt
    text_writer.writerow(["Election Results"])
    text_writer.writerow(["Total Votes Cast ==",total_votes,"==",total_pct])
    text_writer.writerow(["Khan Votes =========",candidate1_votes,"==",candidate1_pct])
    text_writer.writerow(["Correy Votes =======",candidate2_votes,"====",candidate2_pct])
    text_writer.writerow(["Li Votes ===========",candidate3_votes,"====",candidate3_pct])
    text_writer.writerow(["O'Tooley Votes =====",candidate4_votes,"====",candidate4_pct])
    text_writer.writerow(["Election Winner ====",winner])