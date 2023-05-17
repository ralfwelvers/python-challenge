# Ralf Welvers
# Module 3 homework - PyBank
# OS: MacOS Ventura 13.3.1 (a)

import os
import csv

budget_data_csv = os.path.join("Resources", "budget_data.csv")

# open and read csv
result = {}
with open(budget_data_csv) as file:
        csv_reader = csv.reader(file, delimiter=",")
        headers = next(csv_reader)  # Read the header row
        for row in csv_reader:
            key = row[0]  # Assuming the first column contains the key
            values = int(row[1])  # Remaining column contains the value
            result[key] = values

# output to terminal
print()
print("Financial Analysis")
print()
print("----------------------------")
print()
print("Total Months:", len(result))
print()
print("Total: $" + str(sum(result.values())))
print()
print("Average Change: $" + str(int(sum(result.values())/len(result))))
print()
print("Greatest Increase in Profits: " + str(list(result.keys())
      [list(result.values()).index(max(result.values()))])+" ($"+str(max(result.values()))+")")
print()
print("Greatest Decrease in Profits: " + str(list(result.keys())
      [list(result.values()).index(min(result.values()))])+" ($"+str(min(result.values()))+")")
print()

# output to text file
output = os.path.join("analysis", "budget_output.txt")
with open(output, 'w') as output_file:

    output_file.write("\n")
    output_file.write("Financial Analysis")
    output_file.write("\n\n")
    output_file.write("----------------------------")
    output_file.write("\n\n")
    output_file.write("Total Months: "+ str(len(result)))
    output_file.write("\n\n")
    output_file.write("Total: $" + str(sum(result.values())))
    output_file.write("\n\n")
    output_file.write("Average Change: $" + str(int(sum(result.values())/len(result))))
    output_file.write("\n\n")
    output_file.write("Greatest Increase in Profits: " + str(list(result.keys())
        [list(result.values()).index(max(result.values()))])+" ($"+str(max(result.values()))+")")
    output_file.write("\n\n")
    output_file.write("Greatest Decrease in Profits: " + str(list(result.keys())
        [list(result.values()).index(min(result.values()))])+" ($"+str(min(result.values()))+")")
    output_file.write("\n\n")



