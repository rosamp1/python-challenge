# Followed Instructor led content and used Chat GPT for further assistance
import os
import csv

csvpath = os.path.join("Resources", "election_data.csv")
output_file = "election_results.txt"

with open(csvpath) as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',')
    csv_header = next(csvreader)

    # Total number of votes cast , complete list of candidates
    rowcount = 0
    votes_per_candidate = {}

    for row in csvreader:
        rowcount += 1
        candidate = row[2]  
        votes_per_candidate[candidate] = votes_per_candidate.get(candidate, 0) + 1

    total_votes = sum(votes_per_candidate.values())

#Assistance from Chat GPT on exporting results onto text file 
    with open(output_file, "w") as file:
        file.write("Election Results\n")
        file.write("-------------------------\n")
        file.write(f"Total number of votes: {rowcount}\n")
        file.write("-------------------------\n")
        file.write("Candidates who received votes:\n")

# percentage of votes and total number of votes , print winner

        for candidate, votes in votes_per_candidate.items():
            vote_percentage = (votes / total_votes) * 100
            result = f"{candidate}: {votes} votes ({vote_percentage:.3f}% of total votes)\n"
            file.write(result)
            print(result, end="")

        file.write("-------------------------\n")
        winner = max(votes_per_candidate, key=votes_per_candidate.get)
        result = f"Winner: {winner}\n"
        file.write(result)
        print(result)

    print(f"Results exported to '{output_file}'")





