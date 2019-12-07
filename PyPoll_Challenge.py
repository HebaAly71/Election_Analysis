# The data we retrieve
# Total number of votes cast
# List of candidates who recieved votes
# % of votes each candidate won
# total number of votes each candidate won
# The winner of the election based on popular vote

import csv
import os
# dir(csv)
# Create a filename variable to a direct or indirect path to the file.
# Assign a variable to load a file from a path.
file_to_load = os.path.join("Resources/election_results.csv")
# Assign a variable to save the file to a path.
file_to_save = os.path.join("analysis", "election_analysis.txt")
# initiate total votes
total_votes = 0
# initialize the candidates list
candidate_options = []
# initialize county list
county_list = []
# Declare the empty dictionary of candidates data.
candidate_votes = {}
# Declare the empty dictionary of county data.
county_votes = {}
# Winning Candidate and Winning Count Tracker
winning_candidate = ""
winning_count = 0
winning_percentage = 0

# Largest County tracker
largest_county = ""
largest_county_count = 0
largest_county_percentage = 0
# Open the election results and read the file.
with open(file_to_load) as election_data:

    # To do: read and analyze the data here.
    # Read the header row.
    file_reader = csv.reader(election_data)
    headers = next(file_reader)
    for row in file_reader:
        total_votes += 1
        candidate_name = row[2]
        county_name = row[1]
        if candidate_name not in candidate_options:
            candidate_options.append(candidate_name)
            # 2. Begin tracking that candidate's vote count.
            candidate_votes[candidate_name] = 0
        # Add a vote to that county's count.
        candidate_votes[candidate_name] += 1
        if county_name not in county_list:
            county_list.append(county_name)
            # 2. Begin tracking that county vote count.
            county_votes[county_name] = 0
        # Add a vote to that county's count.
        county_votes[county_name] += 1
# Save the results to our text file.
with open(file_to_save, "w") as txt_file:
    # Print the final vote count to the terminal.
    election_results = (
        f"\nElection Results\n"
        f"-------------------------\n"
        f"Total Votes: {total_votes:,}\n"
        f"-------------------------\n"
        f"\n"
        f"County Votes\n")
    print(election_results, end="")
    # Save the final vote count to the text file.
    txt_file.write(election_results)
    for county in county_votes:
        # Retrieve county vote count and county percentage.
        county_votes_count = county_votes[county]
        county_vote_percentage = float(county_votes_count) / float(total_votes) * 100
        county_results = (
            f"{county}: {county_vote_percentage:.1f}% ({county_votes_count:,})\n")
        # Print each county voter count and percentage to the terminal.
        print(county_results)
        #  Save the county results to our text file.
        txt_file.write(county_results)
        # Determine largest county count, county percentage, and largest county.
        if (county_votes_count > largest_county_count) and (county_vote_percentage > largest_county_percentage):
            largest_county_count = county_votes_count
            largest_county = county
            largest_county_percentage = county_vote_percentage
    # Print the largest county results to the terminal.
    largest_county_summary = (
        f"\n"
        f"-------------------------\n"
        f"Largest County Turnout: {largest_county}\n"
        #f"Winning Vote Count: {winning_count:,}\n"
        #f"Winning Percentage: {winning_percentage:.1f}%\n"
        f"-------------------------\n")
    print(largest_county_summary)
    # Save the largest county results to the text file.
    txt_file.write(largest_county_summary)

    for candidate in candidate_votes:
        # Retrieve vote count and percentage.
        votes = candidate_votes[candidate]
        vote_percentage = float(votes) / float(total_votes) * 100
        candidate_results = (
            f"{candidate}: {vote_percentage:.1f}% ({votes:,})\n")

        # Print each candidate's voter count and percentage to the terminal.
        print(candidate_results)
        #  Save the candidate results to our text file.
        txt_file.write(candidate_results)
        # Determine winning vote count, winning percentage, and winning candidate.
        if (votes > winning_count) and (vote_percentage > winning_percentage):
            winning_count = votes
            winning_candidate = candidate
            winning_percentage = vote_percentage
    # Print the winning candidate's results to the terminal.
    winning_candidate_summary = (
        f"-------------------------\n"
        f"Winner: {winning_candidate}\n"
        f"Winning Vote Count: {winning_count:,}\n"
        f"Winning Percentage: {winning_percentage:.1f}%\n"
        f"-------------------------\n")
    print(winning_candidate_summary)
    # Save the winning candidate's results to the text file.
    txt_file.write(winning_candidate_summary)






"""
for candidate in candidate_votes:
    # 2. Retrieve vote count of a candidate.
    votes = candidate_votes[candidate]
    # 3. Calculate the percentage of votes.
    vote_percentage = float(votes) / float(total_votes) * 100
    # 4. Print the candidate name and percentage of votes.
    # Determine winning vote count and candidate
    # Determine if the votes is greater than the winning count.
    if (votes > winning_count) and (vote_percentage > winning_percentage):
         # If true then set winning_count = votes and winning_percent =
         # vote_percentage.
         winning_count = votes
         winning_percentage = vote_percentage
         # And, set the winning_candidate equal to the candidate's name.
         winning_candidate = candidate
    print(f"{candidate}: {vote_percentage:.1f}% ({votes:,})\n")
winning_candidate_summary = (
    f"-------------------------\n"
    f"Winner: {winning_candidate}\n"
    f"Winning Vote Count: {winning_count:,}\n"
    f"Winning Percentage: {winning_percentage:.1f}%\n"
    f"-------------------------\n")
print(winning_candidate_summary)
print(f'The total votes are {total_votes}')
print(f'The candidate list is\n {candidate_options}')
print(candidate_votes)



file_to_save = os.path.join("analysis", "election_analysis.txt")
# Using the open() function with the "w" mode we will write data to the file.
with open(file_to_save, "w") as txt_file:
    #txt_file.write("hello world!")
    txt_file.write("Contains in the election\n----------------------------------\n")
    txt_file.write("Arapahoe\nDenver\nJefferson")
#outfile.close()
#print(election_data)
"""
