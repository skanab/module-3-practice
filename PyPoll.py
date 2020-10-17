import os
import csv

#Setup the files we want to read and write to.
file_to_load = os.path.join("Resources", "election_results.csv")
file_to_save = os.path.join("Analysis", "election_analysis.txt")

total_votes = 0
candidate_options = []
candidate_votes = {}
winning_candidate = ""
winning_count = 0
winning_percentage = 0


#Read File
with open(file_to_load) as election_data:
    file_reader = csv.reader(election_data)

    headers = next(file_reader)
    # print(headers)

    for vote in file_reader:
        #count numer of votes
        total_votes += 1

        canidate_name = vote[2]
        #add canidate if not in list
        if canidate_name not in candidate_options:
            candidate_votes[canidate_name] = 0
            candidate_options.append(canidate_name)
        candidate_votes[canidate_name] += 1

        


for candidate in candidate_votes.keys():
    votes = candidate_votes[candidate]
    vote_percentage = votes / total_votes * 100
    print(f"{candidate}: {vote_percentage:.1f}% ({votes:,})\n")
    if votes > winning_count:
        winning_count = votes
        winning_candidate = candidate
        winning_percentage = vote_percentage

winning_candidate_summary = (
    f"-------------------------\n"
    f"Winner: {winning_candidate}\n"
    f"Winning Vote Count: {winning_count:,}\n"
    f"Winning Percentage: {winning_percentage:.1f}%\n"
    f"-------------------------\n")
print(winning_candidate_summary)

#Write File
with open(file_to_save, 'w') as election_analysis:
    election_analysis.write("Hello World!")

# print(winning_candidate)
# print(winning_count)
# print(winning_percentage)