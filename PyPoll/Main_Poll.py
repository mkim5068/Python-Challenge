import os
import csv

election_data = os.path.join("election_data.csv")

with open(election_data, "r", newline="") as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")
    csv_header = next(csvfile)

    total_votes = 0
    candidates = []
    candidate_votes = []
    votes_percentage = []

    for row in csvreader:
        total_votes += 1

        if row[2] not in candidates:
            candidates.append(row[2])
            candidate_votes.append(1)
        else:
            index = candidates.index(row[2])
            candidate_votes[index] += 1
    
    for votes in candidate_votes:
        percentage = round((votes/ total_votes) * 100)
        votes_percentage.append(percentage)

    winner_votes = max(candidate_votes)
    index = candidate_votes.index(winner_votes)
    winner = candidates[index]

    print(f"Election Results")
    print("---------------------------------")
    print(f"Total Votes: {total_votes}")
    print("---------------------------------")
    for i in range(len(candidates)):
        print(f"{candidates[i]}: {votes_percentage[i]}% ({candidate_votes[i]})")
    print(f"Winner: {winner}")
    print("---------------------------------")

    file = open("output.txt", "w")
    file.write(f"Election Results" + "\n")
    file.write("---------------------------------" + "\n")
    file.write(f"Total Votes: {total_votes}" + "\n")
    file.write("---------------------------------" + "\n") 
    for i in range(len(candidates)):
        file.write(f"{candidates[i]}: {votes_percentage[i]}% ({candidate_votes[i]})" + "\n")
    file.write(f"Winner: {winner}" + "\n")
    file.write("---------------------------------")

    


   

