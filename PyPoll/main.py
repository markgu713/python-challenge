import os
import csv

csvpath = os.path.join("..", "PyPoll", "Resources", "election_data.csv")

votesByCandidate = {}

with open(csvpath, encoding='utf-8') as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',')
    csvheader = next(csvreader)

    # add candidates and his/her votes in a dictionary
    for row in csvreader:
        candidate = row[2]
        if candidate in votesByCandidate:
            votesByCandidate[candidate] = votesByCandidate[candidate] + 1
        else:
            votesByCandidate[candidate] = 1

    # calculate the total votes by looking up the dictionary
    sumOfVotes = 0
    for key in votesByCandidate:
        sumOfVotes = sumOfVotes + votesByCandidate[key]

print("Election Results")
print("------------------------")
print(f"Total Votes: {sumOfVotes}")
print("------------------------")
# calculate and print the % of votes for each candidate
for key in votesByCandidate:
    votePct = "{:.3f}".format(votesByCandidate[key]/sumOfVotes*100)
    print(f"{key}: {votePct}% ({votesByCandidate[key]})")
print("------------------------")
# find the max value in the dict and return the key
max_value = max(votesByCandidate.values())
max_keys = [key for key, value in votesByCandidate.items() if value == max_value]
print(f"Winner: {max_keys[0]}")
print("------------------------")

# export the results to a text file
output_text_path = os.path.join("..", "PyPoll", "analysis", "election_output.txt")

with open(output_text_path, "w") as outputfile:
    outputfile.writelines("Election Results\n")
    outputfile.writelines("------------------------\n")
    outputfile.writelines(f"Total Votes: {sumOfVotes}\n")
    outputfile.writelines("------------------------\n")
    for key in votesByCandidate:
        votePct = "{:.3f}".format(votesByCandidate[key]/sumOfVotes*100)
        outputfile.writelines(f"{key}: {votePct}% ({votesByCandidate[key]})\n")
    outputfile.writelines("------------------------\n")
    outputfile.writelines(f"Winner: {max_keys[0]}\n")
    outputfile.writelines("------------------------\n")
