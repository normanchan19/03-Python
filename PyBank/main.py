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

# ---------------------------------------------- Code Begins ----------------------------------------------

# Import modules
import os
import csv

# Set file path
csvpath = os.path.join('Resources', 'budget_data.csv')

# List of months and years
ListOfMonthsAndYears = []
# List to track monthly change in profit/loss
ChangeInProfitLosses = []
# Set TotalMonthsCounter to 0
TotalMonthsCounter = 0
# Set NetTotalProfitLosses to 0
NetTotalProfitLosses = 0
# Set LastMonthProfitLosses to 0
LastMonthProfitLosses = 0
# Set GreatestIncreaseInProfits to 0
GreatestIncreaseInProfits = 0
# Set GreatestDecreaseInProfits to 0
GreatestDecreaseInProfits = 0

    # Be careful when calculating average profit/loss because TotalMonthsCounter should be n-1 in order to properly account for first
    # month not counting


# Open csv file
with open(csvpath) as csvfile:
    csvreader = csv.reader(csvfile, delimiter = ',')

    next(csvreader)

    # Loop through rows in csv file
    for row in csvreader:
        
        ## Finding Number of Months and Net Profit/Losses

        # Add month and year to ListOfMonthsAndYears
        ListOfMonthsAndYears.append(row[0])

        # Add 1 month to TotalMonthsCounter
        TotalMonthsCounter = TotalMonthsCounter + 1

        # Add monthly Profit/Loss to NetTotalProfitLosses
        NetTotalProfitLosses = NetTotalProfitLosses + int(row[1])
        
        # Add current monthly change in profit/loss to ChangeInProfitLosses
        ChangeInProfitLosses.append(int(row[1]) - LastMonthProfitLosses)

        # Set LastMonthProfitLosses to next value (in preparation of next loop)
        LastMonthProfitLosses = int(row[1])
    
    #---------------------------------------------

    ## Finding Greatest Increase In Profits

    # Find greatest increase in profits
    GreatestIncreaseInProfits = max(ChangeInProfitLosses)

    # Find index of GreatestIncreaseInProfits
    IndexOfGreatestIncreaseInProfits = ChangeInProfitLosses.index(GreatestIncreaseInProfits)

    # Match GreatestIncreaseInProfits to its month and year
    MonthOfGreatestIncreaseInProfits = ListOfMonthsAndYears[IndexOfGreatestIncreaseInProfits]

    #---------------------------------------------

    ## Finding Greatest Decrease In Profits

    # Find greatest decrease in profits
    GreatestDecreaseInProfits = min(ChangeInProfitLosses)

    # Find index of GreatestDecreaseInProfits
    IndexOfGreatestDecreaseInProfits = ChangeInProfitLosses.index(GreatestDecreaseInProfits)

    # Match GreatestDecreaseInProfits to its month and year
    MonthOfGreatestDecreaseInProfits = ListOfMonthsAndYears[IndexOfGreatestDecreaseInProfits]

    #---------------------------------------------

    ## Finding Average Change

    # Remove first month from ChangeInProfitLosses
    ChangeInProfitLosses.pop(0)

    # Calculate average change in profit/losses
    AverageChangeInProfitLosses = round((sum(ChangeInProfitLosses)) / (TotalMonthsCounter - 1), 2)
    

#---------------------------------------------

# Print results in terminal

# print("Financial Analysis")
# print("----------------------------")
# print("Total Months: " + str(TotalMonthsCounter))
# print("Total: $" + str(NetTotalProfitLosses))
# print("Average Change: $" + str(AverageChangeInProfitLosses))
# print("Greatest Increase in Profits: " + MonthOfGreatestIncreaseInProfits + " $" + str(GreatestIncreaseInProfits))
# print("Greatest Decrease in Profits: " + MonthOfGreatestDecreaseInProfits + " $" + str(GreatestDecreaseInProfits))
# print("----------------------------")

# Export results in text file

file = open("PyBankResults.txt", "w")

file.write("Financial Analysis\n")
file.write("----------------------------\n")
file.write("Total Months: " + str(TotalMonthsCounter) + "\n")
file.write("Total: $" + str(NetTotalProfitLosses) + "\n")
file.write("Average Change: $" + str(AverageChangeInProfitLosses) + "\n")
file.write("Greatest Increase in Profits: " + MonthOfGreatestIncreaseInProfits + " $" + str(GreatestIncreaseInProfits) + "\n")
file.write("Greatest Decrease in Profits: " + MonthOfGreatestDecreaseInProfits + " $" + str(GreatestDecreaseInProfits) + "\n")
file.write("----------------------------")