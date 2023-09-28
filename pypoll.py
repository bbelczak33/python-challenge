import os
import csv

# Set path for file
csvpath = os.path.join("Resources/election_data.csv")
txtpath = os.path.join("analysis/election_analysis.txt")

# Places to store data
candidate_votes = {}
vote_percentage = []
candidate_names = []
candidate_v = []
final_candidate = {}
candidates = {}
pnv = []
total_votes = 0

# Open the CSV using the UTF-8 encoding
with open(csvpath, encoding='UTF-8') as csvfile:
    csv_pypoll = csv.reader(csvfile, delimiter=",")
    header = next(csv_pypoll)
    
    for row in csv_pypoll:
        # Find candidate vote counts
        name = row[2]
        candidate_votes[name] = candidate_votes.get(name, 0) + 1
        
        # Count the total votes cast
        total_votes = total_votes + 1
        

for key, value in candidate_votes.items():
    # Create string of candidate names
    i = str(key)
    candidate_names.append(i)
    
    #Create string of candidate vote totals
    j = int(value)
    candidate_v.append(j)
    
    # Find and create string of percentage of votes
    percent = round(value/total_votes * 100, 3)
    vote_percentage.append(f'{float(percent)}%')
    
#Combine percentages with vote totals
for i in range(3):
    pnv = str(vote_percentage[i] + f' ({candidate_v[i]})')
    
#Create dictionary containing all final values
candidates = dict(zip(candidate_names, pnv))
    
# Create new dictionary with candidate names and their votes  
final_candidate = dict(zip(candidate_names, candidate_v))

#Create object with value of winning number of votes
max_votes = max(candidate_v)

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
        # cand_percent = list(final_candidate)
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