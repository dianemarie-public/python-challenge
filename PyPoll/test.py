import os
import csv
import collections

csv_path = os.path.join('Resources', 'election_data.csv')
text_path = os.path.join("Analysis", "election_results.txt")

csv_file_name = 'election_data.csv'
txt_file_name = 'election_reslts.txt'

candidate_votes = collections.Counter()
total_votes = 0

with open(csv_path, 'r') as csvfile:
    csv_reader = csv.DictReader(csvfile)
    next(csv_reader) # Skips header row
    for row in csv_reader:
        candidate_votes[row['Candidate']] += 1 # Returns
        total_votes = candidate_votes 

print(total_votes) # Prints Counter({'A': #, 'B': #, etc.}
print(candidate_votes.most_common()) # Prints list as series

        
    
