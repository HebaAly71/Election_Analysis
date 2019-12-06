# The data we retrieve
# Total number of votes cast
# List of candidates who recieved votes
# % of votes each candidate won
# total number of votes each candidate won
# The winner of the election based on popular vote

import csv
import os
#dir(csv)
# Create a filename variable to a direct or indirect path to the file.
# Assign a variable to load a file from a path.
file_to_load = os.path.join("Resources/election_results.csv")
# Assign a variable to save the file to a path.
file_to_save = os.path.join("analysis", "election_analysis.txt")

# Open the election results and read the file.
with open(file_to_load) as election_data:

    # To do: read and analyze the data here. 

    file_reader = csv.reader(election_data)
    #for row in file_reader:
     #   print(row)
# Print the header row.
    headers = next(file_reader)
    print(headers)








"""
file_to_save = os.path.join("analysis", "election_analysis.txt")
# Using the open() function with the "w" mode we will write data to the file.
with open(file_to_save, "w") as txt_file:
    #txt_file.write("hello world!")
    txt_file.write("Contains in the election\n----------------------------------\n")
    txt_file.write("Arapahoe\nDenver\nJefferson")
#outfile.close()
#print(election_data)
"""
