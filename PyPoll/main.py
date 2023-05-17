# Ralf Welvers
# Module 3 homework - PyPoll
# OS: MacOS Ventura 13.3.1 (a)

import os
import csv

election_data_csv = os.path.join("Resources", "election_data.csv")

# open and read csv
result = []
with open(election_data_csv, 'r') as file:
        csv_reader = csv.reader(file)
        headers = next(csv_reader)  # Read the header row
        for row in csv_reader:
            result.append(row[2]) # only need to grab the names

from collections import Counter

# count the votes
count_votes = dict(Counter(result))
total_votes=sum(count_votes.values())

# output to terminal
print()
print("Election Results")
print()
print("-------------------------")
print()
print("Total Votes: " + str(total_votes))
print()
print("-------------------------")
print()

for k,v in count_votes.items():
    percent_total = v / total_votes
    print(k + ": " + str(format(percent_total, '.3%')) + " (" + str(v) + ")")
    print()

print("-------------------------")
print()
print("Winner: " + str(list(count_votes.keys())
      [list(count_votes.values()).index(max(count_votes.values()))]))
print()
print("-------------------------")
print()

# output to text file
output = os.path.join("analysis", "election_output.txt")
with open(output, 'w') as output_file:
    
    output_file.write("\n\n")
    output_file.write("Election Results")
    output_file.write("\n\n")
    output_file.write("-------------------------")
    output_file.write("\n\n")
    output_file.write("Total Votes: " + str(total_votes))
    output_file.write("\n\n")
    output_file.write("-------------------------")
    output_file.write("\n\n")

    for k,v in count_votes.items():
        percent_total = v / total_votes
        output_file.write(k + ": " + str(format(percent_total, '.3%')) + " (" + str(v) + ")")
        output_file.write("\n\n")

    output_file.write("-------------------------")
    output_file.write("\n\n")
    output_file.write("Winner: " + str(list(count_votes.keys())
        [list(count_votes.values()).index(max(count_votes.values()))]))
    output_file.write("\n\n")
    output_file.write("-------------------------")
    output_file.write("\n\n")


