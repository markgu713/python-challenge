import os
import csv

csvpath = os.path.join("..", "PyBank", "Resources", "budget_data.csv")

date= []
change = []

with open(csvpath, encoding='utf-8') as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',')
    csvheader = next(csvreader)
    # return total number of months and sum of profit/loss
    numOfMonth = 0
    sumOfPnL = 0
    for row in csvreader:
        numOfMonth = numOfMonth + 1
        sumOfPnL = sumOfPnL + float(row[1])
        if numOfMonth > 1: 
            mtmChange = float(row[1]) - pnl
            change.append(mtmChange)
            date.append(row[0])
        pnl = float(row[1])
    # return avg of the change list
    avgChange = round(sum(change) / len(change),2)
    # return date for the greatest increase
    max_value = max(change)
    max_index = change.index(max_value)
    max_date = date[max_index]
    # return date for the greatest decrease
    min_value = min(change)
    min_index = change.index(min_value)
    min_date = date[min_index]

print("Financial Analysis")
print("------------------------")
print(f"Total Month: {numOfMonth}")
print(f"Total: ${round(sumOfPnL)}")
print(f"Average  Change: ${avgChange}")
print(f"Greatest Increase in Profits: {max_date} (${round(max_value)})")
print(f"Greatest Decrease in Profits: {min_date} (${round(min_value)})")

output_text_path = os.path.join("..", "PyBank", "analysis", "financial_analysis_output.txt")

with open(output_text_path, "w") as outputfile:
    outputfile.writelines("Financial Analysis\n")
    outputfile.writelines("------------------------\n")
    outputfile.writelines(f"Total Month: {numOfMonth}\n")
    outputfile.writelines(f"Total: ${round(sumOfPnL)}\n")
    outputfile.writelines(f"Average  Change: ${avgChange}\n")
    outputfile.writelines(f"Greatest Increase in Profits: {max_date} (${round(max_value)})\n")
    outputfile.writelines(f"Greatest Decrease in Profits: {min_date} (${round(min_value)})\n")