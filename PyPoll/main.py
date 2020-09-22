## PyPoll

# In this challenge, you are tasked with helping a small, rural town modernize its vote counting process.

# You will be give a set of poll data called [election_data.csv](PyPoll/Resources/election_data.csv). The dataset is composed of three columns: `Voter ID`, `County`, and `Candidate`. 

# Your task is to create a Python script that analyzes the votes and calculates each of the following:

#   * The total number of votes cast
#   * A complete list of candidates who received votes
#   * The percentage of votes each candidate won
#   * The total number of votes each candidate won
#   * The winner of the election based on popular vote.

import os
import csv

csv_path = os.path.join('Resources', 'election_data.csv')
text_path = os.path.join("Analysis", "election_results.txt")

csv_file_name = 'election_data.csv'
txt_file_name = 'election_reslts.txt'

total_votes = 0
candidate_votes = 0
pct_candidate_votes = 0
num_candidate_votes =0
win_most_votes = 0

with open(csv_path, 'r') as csvfile:
    csv_reader = csv.DictReader(csvfile)
    for row in csv_reader:
        voter_id = int(row["Voter ID"])
        
    total_votes = csv_reader.line_num - 1

    # Formats variables before printing
    total_votes = "{:,.0f}".format(total_votes)
    candidate_votes = "{:,.0f}".format(candidate_votes)
    pct_candidate_votes = "{:,.0f}%".format(pct_candidate_votes)
    num_candidate_votes = "{:,.0f}".format(num_candidate_votes)
    win_most_votes = "{:,.0f}".format(win_most_votes)

    # Prints to terminal
    print(f"Election Results")
    print(f"Total Votes Cast: {total_votes}")
    print(f"Candidates With Votes: {candidate_votes}")
    print(f"Candidate Vote Percent: {pct_candidate_votes}")
    print(f"Candidate Vote Total: {num_candidate_votes}")
    print(f"Candidate With Most Votes: {win_most_votes}")

with open (text_path, "w", newline='') as csvfile:
    text_writer = csv.writer(csvfile, delimiter=' ', quotechar=' ', quoting=csv.QUOTE_MINIMAL)

    # Prints to election_results.txt
    text_writer.writerow(['Election Results'])
    text_writer.writerow(['Total Votes Cast: ',total_votes])
    text_writer.writerow(['Candidates With Votes: ',candidate_votes])
    text_writer.writerow(['Candidate Vote Percent: ',pct_candidate_votes])
    text_writer.writerow(['Candidate Vote Total: ',num_candidate_votes])
    text_writer.writerow(['Candidate With Most Votes: ',win_most_votes])