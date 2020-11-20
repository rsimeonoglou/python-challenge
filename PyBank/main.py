# import modules

import os
import csv

budget_csv = os.path.join("Resources","budget_data.csv")


    

with open(budget_csv, 'r') as csvfile:

    # Split the data on commas
    csvreader = csv.reader(csvfile, delimiter=',')

    #make the first row the header
    header = next(csvreader)
    #make the next row the first row attribute
    firstrow = next(csvreader)

    #define attributes

    Months = 0
    NetTotal = 0
    change = 0
    change_amount = 0
    first_row_profit = int(firstrow[1])
    firstrow.append(0)
    max_value = int(firstrow[2])
    maxrowdate = str(firstrow[0])
    min_value = int(firstrow[2])
    minrowdate = str(firstrow[0])

    #loop through CSV by row

    for row in csvreader:
        
        Months +=1
        NetTotal += int(row[1])
        change = int(row[1]) - int(firstrow[1])
        row.append(change)

        if max_value > int(row[2]):
            maxrowdate = maxrowdate
            max_value = max_value
        else:
            maxrowdate = row[0]
            max_value = row[2]

        if min_value < int(row[2]):
            minrowdate = minrowdate
            min_value = min_value
        else:
            minrowdate = row[0]
            min_value = row[2]

        firstrow = row
        change_amount = change_amount + row[2]    
        
     
#calculations 
    final_months = Months + 1
    final_total = NetTotal + first_row_profit
    average_change = round(change_amount/(final_months - 1),2)

#print financial analysis
    print('Financial Analysis')
    print(f'~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~')
    print(f'Total Months: {final_months}')
    print(f'Total: ${final_total}')
    print(f'Average Change: ${average_change}')
    print(f'Greatest Increase in Profits: {maxrowdate} (${max_value})')
    print(f'Greatest Decrease in Profits: {minrowdate} (${min_value})')



#write the financial analysis to a txt file
import os.path

outputpath = os.path.join("Analysis","analysis.txt")

output = open(outputpath,"w")

output.write("Financial Analysis\n")
output.write(f'~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~\n')
output.write(f'Total Months: {final_months}\n')
output.write(f'Total: ${final_total}\n')
output.write(f'Average Change: ${average_change}\n')
output.write(f'Greatest Increase in Profits: {maxrowdate} (${max_value})\n')
output.write(f'Greatest Decrease in Profits: {minrowdate} (${min_value})\n')

output.close()