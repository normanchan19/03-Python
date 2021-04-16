# ## PyPoll

# ![Vote Counting](Images/Vote_counting.png)

# * In this challenge, you are tasked with helping a small, rural town modernize its vote counting process.

# * You will be give a set of poll data called [election_data.csv](PyPoll/Resources/election_data.csv). The dataset is composed of three columns: `Voter ID`, `County`, and `Candidate`. Your task is to create a Python script that analyzes the votes and calculates each of the following:

#   * The total number of votes cast

#   * A complete list of candidates who received votes

#   * The percentage of votes each candidate won

#   * The total number of votes each candidate won

#   * The winner of the election based on popular vote.

# * As an example, your analysis should look similar to the one below:

#   ```text
#   Election Results
#   -------------------------
#   Total Votes: 3521001
#   -------------------------
#   Khan: 63.000% (2218231)
#   Correy: 20.000% (704200)
#   Li: 14.000% (492940)
#   O'Tooley: 3.000% (105630)
#   -------------------------
#   Winner: Khan
#   -------------------------
#   ```

# * In addition, your final script should both print the analysis to the terminal and export a text file with the results.

# ---------------------------------------------- Code Begins ----------------------------------------------

# Import modules
import os
import csv

# Set file path
csvpath = os.path.join('Resources', 'election_data.csv')

# Create dictionary with candidate as key and votes received as value
CandidatesAndVotes = {}
# Candidates is just candidate names
Candidates = []
# List of just vote numbers for each candidate
Votes = []
# List of vote percentages for each candidate
VotePercentage = []

# Open csv file
with open(csvpath) as csvfile:
    csvreader = csv.reader(csvfile, delimiter = ',')

    next(csvreader)

    # Loop through rows in csv file
    for row in csvreader:

        # If candidate is already in dictionary

        if row[2] in CandidatesAndVotes:

            # Add a vote to the candidate's value
            CandidatesAndVotes[row[2]] += 1

        else:

            # Add new candidate to dictionary and set value to 1
            CandidatesAndVotes[row[2]] = 1
        
    # Find total votes cast in whole election
    TotalVotes = sum(CandidatesAndVotes.values())

    # Candidates is list of candidates
    Candidates = list(CandidatesAndVotes.keys())

    # Votes is list of vote number for each candidate
    Votes = list(CandidatesAndVotes.values())

    # Convert Votes list into vote percentage
    VotePercentage = [round(i / TotalVotes * 100, 3) for i in Votes]

    # Determine winner of election based on who got highest percent vote
    Winner = Candidates[VotePercentage.index(max(VotePercentage))]

#---------------------------------------------

# Print results in terminal

print("Election Results")
print("-------------------------")
print("Total Votes:" + str(TotalVotes))
print("-------------------------")
for i in range(len(Candidates)):
    print(Candidates[i] + ":" + str(VotePercentage[i]) + "%" + " (" + str(Votes[i]) + ")")
print("-------------------------")
print("Winner: " + Winner)

#---------------------------------------------

# Export results in text file

file = open("PyPollResults.txt", "w")

file.write("Election Results\n")
file.write("-------------------------\n")
file.write("Total Votes:" + str(TotalVotes) + "\n")
file.write("-------------------------\n")
for i in range(len(Candidates)):
    file.write(Candidates[i] + ":" + str(VotePercentage[i]) + "%" + " (" + str(Votes[i]) + ")\n")
file.write("-------------------------\n")
file.write("Winner: " + Winner)