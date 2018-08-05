import os
import csv

csvpath = os.path.join('Resources', 'election_data.csv')
output_file = "main.txt"

#Variables
candidate_name="unknown"
votes=0
total_votes=0
most_votes=0
winning_votes=0
winning_candidate=""
candidate_vote_summary=""

#list to hold all unique candidates
candidate_options = []
#dictionary to track candidates and their corresponding votes
candidate_votes = {}

with open(csvpath) as election_data:
	csvreader = csv.reader(election_data, delimiter=",")
	next(csvreader, None)

	for row in csvreader:
		total_votes=total_votes+1
		candidate_name=row[2]

# A complete list of candidates who received votes
	#creating a dictionary entry on the first occurence of candidate name
		if candidate_name not in candidate_options:
			candidate_options.append(candidate_name)
			candidate_votes[candidate_name] = 0
	#if candidate_name already in cadidate_votes, increment vote by 1
	candidate_votes[candidate_name] = candidate_votes[candidate_name] + 1
# calculate total number of votes per candidate
	for votes in candidate_votes.values():
		total_votes = total_votes + votes 


	for candidate_name in candidate_votes:
		votes = candidate_votes[candidate_name]
		vote_percent = float(votes)/float(total_votes)*100

		if votes > winning_votes:
			winning_votes = votes
			winning_candidate = candidate_name

		candidate_vote_summary = candidate_vote_summary + f"{candidate_name} : {vote_percent: .3f}%({votes}) \n"

	







# print results
output = (
	f"Election Results \n"
	f"-------------------------------- \n"
	f"Total Votes: {total_votes} \n"
	f"-------------------------------- \n"
	f"{candidate_vote_summary} \n"
	f"-------------------------------- \n"
	f"Winner: {winning_candidate} \n"
	f"-------------------------------- \n")

print(output)

#export to txt file
with open(output_file, "w") as txt_file:
	txt_file.write(output)

