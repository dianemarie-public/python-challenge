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
text_path = os.path.join('Analysis', 'output.txt')

file_name = 'election_data.csv'

election_dictionary = {}

total_votes_cast = 0
candidate_votes = 0
pct_candidate_votes = 0
num_candidate_votes =0
winner_most_votes = 0

with open(csv_path, 'r') as csvfile:
    csv_reader = csv.DictReader(csvfile)
    for row in csv_reader:
        voter_id = int(row["Voter ID"])
        
total_votes_cast = csv_reader.line_num - 1
print(total_votes_cast)
