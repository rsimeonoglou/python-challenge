# import modules

import os
import csv

election_csv = os.path.join("Resources","election_data.csv")

with open(election_csv, 'r') as csvfile:

    # Split the data on commas
    csvreader = csv.reader(csvfile, delimiter=',')

    #make first row the header
    header = next(csvreader)

    #designate attributes
    votes = 0
    Khan = 0
    Correy = 0
    Li = 0
    O_Tooley = 0

    #loop through CSV
    for row in csvreader:
        
        votes +=1
        if row[2] == "Khan":
            Khan = Khan + 1

        elif row[2] == "Correy":
            Correy = Correy + 1
            
        elif row[2] == "Li":
            Li = Li + 1

        else:
            O_Tooley = O_Tooley + 1

    
    #calculations
    khan_percent = round((Khan/votes)*100,3)
    correy_percent = round((Correy/votes)*100,3)
    li_percent = round((Li/votes)*100,3)
    o_tooley_percent = round((O_Tooley/votes)*100,3)

    #find winner by most votes
    if Khan > Correy and Khan > Li and Khan > O_Tooley:
        winner = "Khan"
    elif Correy > Khan and Correy > Li and Correy > O_Tooley:
        winner = "Correy"
    elif Li > Khan and Li > Correy and Li > O_Tooley:
        winner = "Li"
    else:
        winner = "O'Tooley"

    #print Results
    print(f'Election Results')
    print(f'~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~')
    print(f'Total Votes: {votes}')
    print(f'~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~')
    print(f'Khan: {khan_percent}% ({Khan})')
    print(f'Correy: {correy_percent}% ({Correy})')
    print(f'Li: {li_percent}% ({Li})')
    print(f"O'Tooley: {o_tooley_percent}% ({O_Tooley})")
    print(f'~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~')
    print(f'Winner: {winner}')
    print(f'~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~')

#export results to a txt file
            
import os.path

outputpath = os.path.join("Analysis","analysis.txt")

output = open(outputpath,"w")

output.write(f'Election Results\n')
output.write(f'~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~\n')
output.write(f'Total Votes: {votes}\n')
output.write(f'~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~\n')
output.write(f'Khan: {khan_percent}% ({Khan})\n')
output.write(f'Correy: {correy_percent}% ({Correy})\n')
output.write(f'Li: {li_percent}% ({Li})\n')
output.write(f"O'Tooley: {o_tooley_percent}% ({O_Tooley})\n")
output.write(f'~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~\n')
output.write(f'Winner: {winner}\n')
output.write(f'~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~\n')

output.close()