
# Ralf Welvers
# Module 3 homework - PyBank
# OS: MacOS Ventura 13.3.1 (a)

import os
import csv

budget_data_csv = os.path.join("Resources", "budget_data.csv")

# open and read csv
result = {}
change = {}
with open(budget_data_csv) as file:
        csv_reader = csv.reader(file, delimiter=",")
        headers = next(csv_reader)  # Read the header row

        for row in csv_reader:
            key = row[0]  # Assuming the first column contains the key
            values = int(row[1])  # Remaining column contains the value
            result[key] = values

value_previous = list(result.values())[0]
# print(value_compare)

dict_len = len(result)
# loop through the values and calculate each change. store in a new dictionary
for x in range(1,dict_len):
    key_grab = str(list(result)[x])
    value_next = list(result.values())[x]
    change_value = value_next - value_previous
    change[key_grab] = change_value
    value_previous = value_next

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
average_change = sum(change.values())/len(change)
print("Average Change: ${:.2f}".format(average_change))
print()
print("Greatest Increase in Profits: " + str(list(change.keys())
      [list(change.values()).index(max(change.values()))])+" ($"+str(max(change.values()))+")")
print()
print("Greatest Decrease in Profits: " + str(list(change.keys())
      [list(change.values()).index(min(change.values()))])+" ($"+str(min(change.values()))+")")


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
    output_file.write("Average Change: ${:.2f}".format(average_change))
    output_file.write("\n\n")
    output_file.write("Greatest Increase in Profits: " + str(list(change.keys())
      [list(change.values()).index(max(change.values()))])+" ($"+str(max(change.values()))+")")
    output_file.write("\n\n")
    output_file.write("Greatest Decrease in Profits: " + str(list(change.keys())
      [list(change.values()).index(min(change.values()))])+" ($"+str(min(change.values()))+")")
  
