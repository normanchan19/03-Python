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

# Set variables
CandidatesAndVotes = {}
ZeroVote = 0

# Open csv file
with open(csvpath) as csvfile:
    csvreader = csv.reader(csvfile, delimiter = ',')

    next(csvreader)

    # Loop through rows in csv file
    for row in csvreader:
        if row[2] in CandidatesAndVotes:
            CandidatesAndVotes[row[2]] += 1
        else:
            CandidatesAndVotes[row[2]] = 1
        
    TotalVotes = sum(CandidatesAndVotes.values())
        # NORMAN USE DICTIONARIES, CANDIDATE IS KEY AND VOTES ARE VALUES

print(TotalVotes)
print(CandidatesAndVotes.items())