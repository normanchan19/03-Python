# ## PyBank

# ![Revenue](Images/revenue-per-lead.png)

# * In this challenge, you are tasked with creating a Python script for analyzing the financial records of your company. You will give a set of financial data called [budget_data.csv](PyBank/Resources/budget_data.csv). The dataset is composed of two columns: `Date` and `Profit/Losses`. (Thankfully, your company has rather lax standards for accounting so the records are simple.)

# * Your task is to create a Python script that analyzes the records to calculate each of the following:

#   * The total number of months included in the dataset

#   * The net total amount of "Profit/Losses" over the entire period

#   * Calculate the changes in "Profit/Losses" over the entire period, then find the average of those changes

#   * The greatest increase in profits (date and amount) over the entire period

#   * The greatest decrease in losses (date and amount) over the entire period

# * As an example, your analysis should look similar to the one below:

#   ```text
#   Financial Analysis
#   ----------------------------
#   Total Months: 86
#   Total: $38382578
#   Average  Change: $-2315.12
#   Greatest Increase in Profits: Feb-2012 ($1926159)
#   Greatest Decrease in Profits: Sep-2013 ($-2196167)
#   ```

# * In addition, your final script should both print the analysis to the terminal and export a text file with the results.

# Import modules
import os
import csv

# Set file path
csvpath = os.path.join('Resources', 'budget_data.csv')

# Set TotalMonthsCounter to 0
TotalMonthsCounter = 0
# Set NetTotalProfitLosses to 0
NetTotalProfitLosses = 0
# Set LastMonthProfitLosses to 0

    # Be careful when calculating average profit/loss because TotalMonthsCounter should be n-1 in order to properly account for first
    # month not counting


# Create new list tracking monthly change in profit/loss


# Open csv file
with open(csvpath) as csvfile:
    csvreader = csv.reader(csvfile, delimiter = ',')

    # Loop through rows in csv file
    for row in csvreader:
        
        # Add 1 month to TotalMonthsCounter
        TotalMonthsCounter = TotalMonthsCounter + 1

        # Add monthly Profit/Loss to NetTotalProfitLosses
        NetTotalProfitLosses = NetTotalProfitLosses + row[1]

        # Calculate monthly change in profit/loss

