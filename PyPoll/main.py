# -*- coding: UTF-8 -*-
"""PyPoll Homework Starter File."""

# Import necessary modules
import os
import csv 
 
# Files to load and output (update with correct file paths)
file_to_load = r"C:\\Users\\carls\Desktop\\Repositories\\python-challenge\\PyPoll\\Resources\\election_data.csv"
file_to_output = r"C:\\Users\\carls\Desktop\\Repositories\\python-challenge\\PyPoll\\analysis\\election_results.txt"
 
# Initialize variables to track the election data
total_votes = 0
# Define lists and dictionaries to track candidate names and vote counts
candidates = {}  

# Winning Candidate and Winning Count Tracker
winner = ""
winning_votes = 0
 
# Open the CSV file and process it
with open(file_to_load, newline="") as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")
 
    # Skip the header row
    csv_header = next(csvreader)
 
    # Loop through each row of the dataset and process it

    # Increment the total vote count for each row
    for row in csvreader:
        total_votes += 1
        candidate = row[2]  
 
        # If the candidate is not already in the candidate list, add them
        if candidate not in candidates:
            candidates[candidate] = 0
 
        # Add a vote to the candidate's count
        candidates[candidate] += 1
 
#Winner
for candidate in candidates:
    votes = candidates[candidate]
    if votes > winning_votes:
        winning_votes = votes
        winner = candidate
 
# Print the total vote count (to terminal)
# Write the total vote count to the text file
print("Election Results")
print("-------------------------")
print(f"Total Votes: {total_votes}")
print("-------------------------")
 
# Loop through the candidates to determine vote percentages and identify the winner
for candidate in candidates:
    votes = candidates[candidate]
    vote_percentage = (votes / total_votes) * 100
    # Print and save each candidate's vote count and percentage
    print(f"{candidate}: {vote_percentage:.3f}% ({votes})")
 
print("-------------------------")
print(f"Winner: {winner}")
print("-------------------------")
 
# Export results to a text file
with open(file_to_output, 'w') as txtfile:
    txtfile.write("Election Results\n")
    txtfile.write("-------------------------\n")
    txtfile.write(f"Total Votes: {total_votes}\n")
    txtfile.write("-------------------------\n")
 
    # Generate and print the winning candidate summary
    # Save the winning candidate summary to the text file
    for candidate in candidates:
        votes = candidates[candidate]
        vote_percentage = (votes / total_votes) * 100
        txtfile.write(f"{candidate}: {vote_percentage:.3f}% ({votes})\n")
 
    txtfile.write("-------------------------\n")
    txtfile.write(f"Winner: {winner}\n")
    txtfile.write("-------------------------\n")
