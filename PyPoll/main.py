import os
import csv

csvpath = os.path.join("..", "PyPoll", "Resources", "election_data.csv")

with open(csvpath, encoding='utf-8') as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',')
    csvheader = next(csvreader)
    # return total number of months and sum of profit/loss
    numOfVotes = 0

    for row in csvreader:
        numOfVotes = numOfVotes + 1

print("Election Results")
print("------------------------")
print(f"Total Votes: {numOfVotes}")
print("------------------------")
#print(f"Total: ${round(sumOfPnL)}")
#print(f"Average  Change: ${avgChange}")
#print(f"Greatest Increase in Profits: {max_date} (${round(max_value)})")
#print(f"Greatest Decrease in Profits: {min_date} (${round(min_value)})")
print("------------------------")
print("------------------------")
#output_text_path = os.path.join("..", "PyBank", "analysis", "financial_analysis_output.txt")

# with open(output_text_path, "w") as outputfile:
    #outputfile.writelines("Financial Analysis\n")
    #outputfile.writelines("------------------------\n")
    #outputfile.writelines(f"Total Month: {numOfMonth}\n")
    #outputfile.writelines(f"Total: ${round(sumOfPnL)}\n")
    #outputfile.writelines(f"Average  Change: ${avgChange}\n")
    #outputfile.writelines(f"Greatest Increase in Profits: {max_date} (${round(max_value)})\n")
    #outputfile.writelines(f"Greatest Decrease in Profits: {min_date} (${round(min_value)})\n")

