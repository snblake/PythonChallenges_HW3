import csv 
import os

all_months = []
profit_loss_change = []

file_path = os.path.join("Resources", "budget_data.csv")
of= open("PybankHW3.txt","w+")

with open(file_path, "r") as f:   
    reader = csv.reader(f)
    next(reader)                                                                        # skips the header row
    first_row = next(reader)
    prev_row_value = first_row[1]
    ctr = int(prev_row_value)                                                           #declare counter variables, list for
    month_ctr = 1                                                                       #report calculations
    all_months.append(first_row[0])
    greatest_dec = 0
    greatest_dec_mon = first_row[0]
    greatest_inc = 0
    greatest_inc_mon = first_row[0]

    for row in (reader):                                                                  #read first row, store values for
        mon_yr = row[0]                                                                   #comparison, store PL change for
        all_months.append(mon_yr)                                                         #calculating change avg
        ctr += int(row[1])
        month_ctr = month_ctr +1
        month_change_val = int(row[1]) - int(prev_row_value)
        profit_loss_change.append(int(month_change_val))
        
        if greatest_dec > month_change_val:
            greatest_dec = month_change_val
            greatest_dec_mon = row[0]
        elif greatest_inc < month_change_val:
            greatest_inc = month_change_val
            greatest_inc_mon = row[0]
        #print(f"int({row[1]}) - int({prev_row_value})") - test 
        prev_row_value = row[1]

    avg_rev_change = "{:.2f}".format(sum(profit_loss_change)/len(profit_loss_change))
    
    print(f" ")                                                                                 #print results
    print(f"Financial Analysis")
    print(f"_" * 25)
    print(f" ")
    print(f"Total Months: {month_ctr}")
    print(f"Total: ${ctr}")
    print(f"Average Change: ${avg_rev_change}")
    print(f"Greatest Increase In Profits: {greatest_inc_mon} (${greatest_inc})")
    print(f"Greatest Decrease in Profits: {greatest_dec_mon} (${greatest_dec})")

    of.write("Financial Analysis\n")                                                            #write report to file
    of.write("_" * 25 + "\n\n")
    of.write("Total Months: " + str(month_ctr) + "\n")
    of.write("Total: $" + str(ctr) + "\n")
    of.write("Average Change: $" + str(avg_rev_change) + "\n")
    of.write("Greatest Increase In Profits: " + str(greatest_inc_mon) + " " + "($" + str(greatest_inc) + ")" + "\n")
    of.write("Greatest Decrease in Profits: " + str(greatest_dec_mon) + " " + "($" + str(greatest_dec) + ")" + "\n")
    of.close
 