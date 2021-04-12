# Import modules
import os
import csv

# Set file path
csvpath = os.path.join('Resources', 'budget_data.csv')

# Set TotalMonthsCounter to 0
TotalMonthsCounter = 0


# Open csv file
with open(csvpath) as csvfile:
    csvreader = csv.reader(csvfile, delimiter = ',')

    