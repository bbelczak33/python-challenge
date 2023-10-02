import os
import csv

# Set path for file
csvpath = os.path.join("Resources/budget_data.csv")
txtpath = os.path.join("analysis/budget_analysis.txt")

# Places to store data
dates = []
pl = []
pl_int = []
total_months = 0
pl_change = []

# Open the CSV using the UTF-8 encoding
with open(csvpath, encoding='UTF-8') as csvfile:
    csv_pybank = csv.reader(csvfile, delimiter=",")
    header = next(csv_pybank)

    for row in csv_pybank:
        # Add dates
        dates.append(row[0])
        
        # Add profits/losses
        pl.append(row[1])
        
        # Calculate total months
        total_months = total_months + 1
        
    for i in pl:
        # Convert pl into integers
        value = int(i)
        pl_int.append(value)
        
    for i in range(1, len(pl_int)):
        # Create list of changes in profit
        value = pl_int[i] - pl_int[i - 1]
        pl_change.append(value)

# Create objects for average, max, and min change and their dates
avg_change = sum(pl_change)/(total_months - 1)
max_change = max(pl_change)
min_change = min(pl_change)
date_max = dates[pl_change.index(max(pl_change)) + 1]
date_min = dates[pl_change.index(min(pl_change)) + 1]

# Create text file
with open(txtpath, 'w') as txtfile:


    output = (
        f'Financial Analysis\n'
        f'----------------\n'
        f'Total Months: {total_months}\n'
        f'Total Profit: ${sum(pl_int)}\n'
        f'Average Change: ${avg_change:.2f}\n'
        f'Greatest Increase in Profits: {date_max} (${max_change})'
        f'Greatest Decrease in Profits: {date_min} (${min_change})'
    )
    print(output)
    txtfile.write(output)