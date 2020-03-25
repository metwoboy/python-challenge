#import modules
import os 
import csv

#Navigate to the targeted file
csvfile = os.path.join("Resources","budget_data.csv")
#output the result to a text file.
pathout = os.path.join("Resources","budget_analysis.txt")

#open csv file
with open(csvfile) as file:
    csvreader = csv.reader(file, delimiter=',')
    
#set variables to zero.
    total_month = 0
    total_amount = 0
    pre_amt = 0
    pl_changes_dict = {}

#skip column header row
    next(csvreader)

#start looping through the rows
    for row in csvreader:
        # loop incremental argument; total month = total month + 1
        total_month +=1

        if total_month ==1:
            #store value of first row into pre_amt
            pre_amt = int(row[1])

        elif total_month >1:
            changes = int(row[1]) - pre_amt
            #store changes into a dictionary
            pl_changes_dict.update({row[0]:changes})
            pre_amt = int(row[1])

        #net total amount of Profit/Losses" over the entire period..
        total_amount= total_amount + pre_amt
    next

    #cal to find average changes
    sum_changes = sum(pl_changes_dict.values())
    average_changes = round(sum_changes/len(pl_changes_dict),2)

    #Find the max and min changes;in addition to the date
    max_changes_dt = max(pl_changes_dict,key=pl_changes_dict.get)
    max_changes_amt = max(pl_changes_dict.values())
    min_changes_dt= min(pl_changes_dict,key=pl_changes_dict.get)
    min_changes_amt = min(pl_changes_dict.values())


    output = (
        '---------------------------------------------------------\n'
        'Financial Analysis\n'
        '---------------------------------------------------------\n'
        f'Total Months  : {total_month}\n'
        f'Total(net P/L): ${total_amount}\n'
        f'Average Change: ${average_changes}\n'
        f'Greatest Increase in Profits: {max_changes_dt} (${max_changes_amt})\n'
        f'Greatest Decrease in Profits: {min_changes_dt} (${min_changes_amt})\n'
    )

    print(output)

#write to the text path
with open(pathout,'w') as txt_file:
    txt_file.write(output)