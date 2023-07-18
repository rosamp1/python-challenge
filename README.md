# python-challenge 
Most of the code used in this challenge came from class sessions however, some content was tweaked using assitance from Chat GPT as well as some code used in challege was also provided by Chat GPT

Below code was provided by Chat GPT: PyPoll Activity

with open(output_file, "w") as file:
        file.write("Election Results\n")
        file.write("-------------------------\n")
        file.write(f"Total number of votes: {rowcount}\n")
        file.write("-------------------------\n")
        file.write("Candidates who received votes:\n")

          file.write("-------------------------\n")
        winner = max(votes_per_candidate, key=votes_per_candidate.get)
        result = f"Winner: {winner}\n"
        file.write(result)
        print(result)

    print(f"Results exported to '{output_file}'")

Initial code was not useable so assistance from Chat GPT was requested
rowcount += 1

Initial code was learned from class session with  some assistance provided in below code from Chat GPT
for candidate, votes in votes_per_candidate.items():
            vote_percentage = (votes / total_votes) * 100
            result = f"{candidate}: {votes} votes ({vote_percentage:.3f}% of total votes)\n"
            file.write(result)
            print(result, end="")

Below code was provided by Chat GPT: PyBank Activity

 Final script should both print the analysis to the terminal and export a text file with the results
    output = f"Total number of line items: {rowcount}\n"
    output += f"Net total amount of 'profit/losses' over the entire period: ${net_total}\n"
    output += f"Changes in 'profit/losses' over the entire period: ${total_changes}\n"
    output += f"Average change in 'profit/losses' over the entire period: ${average_change:.2f}\n"
    output += f"Greatest increase in profits: {greatest_increase_month} (${greatest_increase})\n"
    output += f"Greatest decrease in profits: {greatest_decrease_month} (${greatest_decrease})\n"
    with open(output_file,"w") as file:
            file.write(output)
