import os
import csv

filepath = os.path.join(".", "Resources", "election_data.csv")

candidates = {}
numberofVoters = 0
candidatePercentages = {}
highestnumberofVotes = 0

with open(filepath) as csv_file:
    csv_reader = csv.DictReader(csv_file, delimiter=",")
    for voter in csv_reader:
        numberofVoters = numberofVoters + 1
        candidatevotedFor = voter["Candidate"]

        try:
            candidates[candidatevotedFor] = candidates[candidatevotedFor] + 1

        except: 
            candidates[candidatevotedFor] = 1
for candidate in candidates:
    numberofvotes = candidates[candidate]
    percentage = (numberofvotes / numberofVoters) * 100
    candidatePercentages[candidate] = percentage 
   
    if numberofvotes > highestnumberofVotes:
        highestnumberofVotes = numberofvotes 

print("Election Results")
print("--------------------")
print(f"Total Votes: {numberofVoters}")
print("--------------------")

for candidate in candidates:
    numberofvotes = candidates[candidate]
    if numberofvotes == highestnumberofVotes:
        winner = candidate


    
    
    print(f"{candidate}: {candidatePercentages[candidate]:.3f}% ({numberofvotes})")
print("--------------------")
print(f"Winner: {winner}")
print("--------------------")

writerpath = os.path.join(".", "Resources", "results.txt")

with open(writerpath, "w") as text:
    text.write("Election Result\n")
    text.write("--------------------\n")
    text.write(f"Total Votes: {numberofVoters}\n")
    text.write("--------------------\n")

    for candidate in candidates:
        numberofvotes = candidates[candidate]
        if numberofvotes == highestnumberofVotes:
            winner = candidate


        
        
        text.write(f"{candidate}: {candidatePercentages[candidate]}% ({numberofvotes})\n")
    text.write("--------------------\n")
    text.write(f"Winner: {winner}\n")
    text.write("--------------------\n")

