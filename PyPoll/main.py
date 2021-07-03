import os
import csv

csvpath = os.path.join('Resources','election_data.csv')
total_votes = 0
vote_total = []
candidates_name = []
vote_each = []
vote_percentage = []

with open(csvpath) as election_csv:
    csvreader = csv.reader(election_csv, delimiter=',')
    csv_header =next(csvreader)
    for row in csvreader: 
        total_votes += 1
        if row[2] not in candidates_name:
            candidates_name.append(row[2])
            index = candidates_name.index(row[2])
            vote_each.append(1)
        else:
            index = candidates_name.index(row[2])
            vote_each[index] = vote_each[index] + 1 
    for votes in vote_each:
        percentage = (votes/total_votes)
        percentage = "{:.3%}".format(percentage)
        vote_percentage.append(percentage)
candidate = max(vote_each)
index = vote_each.index(candidate)
winner = candidates_name[index]
print("Election Results")
print("--------------------------")
print("Total Votes: " + str(total_votes))
print("--------------------------")

for i in range(len(candidates_name)):
    print(candidates_name[i] + ": " + (str(vote_percentage[i])) + " (" + (str(vote_each[i])) + ")")
print("--------------------------")
print("Winner: " + winner)
print("--------------------------")
output_path = os.path.join("analysis", "election_results.txt")

with open (output_path,"w") as file:
    file.write ("Election Results")
    file.write ("\n")
    file.write ("----------------------------")
    file.write ("\n")
    file.write (f"Total Votes: " + str(total_votes))
    file.write ("\n")
    file.write ("--------------------------")
    file.write ("\n")

    for i in range(len(candidates_name)):
        line = ((candidates_name[i] + ": " + (str(vote_percentage[i])) + " (" + (str(vote_each[i])) + ")"))
        file.write('{}\n'.format(line))
    file.write ("--------------------------")
    file.write ("\n")
    file.write (f"Winner: " + winner)
    file.write ("\n")
    file.write ("--------------------------")