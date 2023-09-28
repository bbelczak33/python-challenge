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

# Create objects for max and min change dates
date_max = dates[pl_change.index(max(pl_change)) + 1]
date_min = dates[pl_change.index(min(pl_change)) + 1]
        
# Print total months
print("Total Months:", total_months)

# Find and print the total profit
print("Total Profit:", f'${sum(pl_int)}')

# Find and print the average change in profit
print("Average Change:", f'${round(sum(pl_change)/(total_months - 1), 2)}')

# Find and print the greatest increase in profit and its corresponding date
print("Greatest Increase in Profits:", date_max, f'(${max(pl_change)})')

# Find and print the greatest decrease in profit and its corresponding date
print("Greatest Decrease in Profits:", date_min, f'(${min(pl_change)})')

with open(txtpath, 'w') as txtfile:


    output = (
        f'Election Results\n'
        f'----------------\n'
        f'Total Votes: {total_votes}\n'
        f'----------------\n'
    )
    print(output)
    txtfile.write(output)

    for key, value in final_candidate.items():
        #Create lists of candidates and their correspondin number of votes
        cand_nams = list(final_candidate.keys())
        cand_vots = list(final_candidate.values())
        cand_percent = (float(value) / float(total_votes)) * 100
        output = (
            f'{key}: {cand_percent:.3f}% ({value})\n'
        )
        print(output)
        txtfile.write(output)

        #Identify the index of the winning candidate and assign winning name to object
        win_po = cand_vots.index(max_votes)
        winner = cand_nams[win_po]
        
    output = (
        f'----------------\n'
        f'Winner: {winner}\n'
        f'----------------\n'
    )
    print(output)
    txtfile.write(output)