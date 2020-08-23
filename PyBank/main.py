import os
import csv

csvpath = os.path.join("..", "PyBank", "Resources", "budget_data.csv")

with open(csvpath, encoding='utf-8') as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',')
    csvheader = next(csvreader)
    for row in csvreader:
        print(row)


print("Financial Analysis")
print("------------------------")
print(f"Total Month: {len(csvreader)}")
print(f"Total: {len(csvreader)}")
print(f"Average  Change: {len(csvreader)}")
print(f"Greatest Increase in Profits: {len(csvreader)}")
print(f"Greatest Decrease in Profits: {len(csvreader)}")