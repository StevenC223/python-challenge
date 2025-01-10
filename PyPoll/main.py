# Modules
import os
import csv 
 
# Set path for files
file_to_load = r"C:\\Users\\carls\Desktop\\Repositories\\python-challenge\\PyPoll\\Resources\\election_data.csv"
file_to_output = r"C:\\Users\\carls\Desktop\\Repositories\\python-challenge\\PyPoll\\analysis\\election_results.txt"
 
# Initialize variables
total_votes = 0
candidates = {}  # Dictionary to store candidate votes
winner = ""
winning_votes = 0
 
# Read the data from the CSV file
with open(file_to_load, newline="") as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")
 
    # Reading the header row
    csv_header = next(csvreader)
 
    # Process each row
    for row in csvreader:
        total_votes += 1
        candidate = row[2]  # Candidate name is in the third column
 
        # Add candidate to dictionary if not there
        if candidate not in candidates:
            candidates[candidate] = 0
 
        # Add a vote to that candidate's count
        candidates[candidate] += 1
 
# Determine the winner
for candidate in candidates:
    votes = candidates[candidate]
    if votes > winning_votes:
        winning_votes = votes
        winner = candidate
 
# Print the results
print("Election Results")
print("-------------------------")
print(f"Total Votes: {total_votes}")
print("-------------------------")
 
# Calculate and display percentage for each candidate
for candidate in candidates:
    votes = candidates[candidate]
    vote_percentage = (votes / total_votes) * 100
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
 
    # Write each candidate's results
    for candidate in candidates:
        votes = candidates[candidate]
        vote_percentage = (votes / total_votes) * 100
        txtfile.write(f"{candidate}: {vote_percentage:.3f}% ({votes})\n")
 
    txtfile.write("-------------------------\n")
    txtfile.write(f"Winner: {winner}\n")
    txtfile.write("-------------------------\n")