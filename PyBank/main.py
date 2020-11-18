# import modules

import os
import csv

budget_csv = os.path.join("Resources","budget_data.csv")


    

with open(budget_csv, 'r') as csvfile:

    # Split the data on commas
    csvreader = csv.reader(csvfile, delimiter=',')

    header = next(csvreader)
    firstrow = next(csvreader)

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
        
     

    final_months = Months + 1
    final_total = NetTotal + first_row_profit
    average_change = round(change_amount/(final_months - 1),2)


    print('Financial Analysis')
    print(f'~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~')
    print(f'Total Months: {final_months}')
    print(f'Total: ${final_total}')
    print(f'Average Change: ${average_change}')
    print(f'Greatest Increase in Profits: {maxrowdate} (${max_value})')
    print(f'Greatest Decrease in Profits: {minrowdate} (${min_value})')
    


        

    





