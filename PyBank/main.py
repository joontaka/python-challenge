# import packages
import os
import csv

# list declaration
monthyear = []

# set file path for source and output files
sourcepath = os.path.join("Resources", "budget_data.csv")
resultpath = os.path.join("analysis", "result.txt")

# open and read csv file handler
with open (sourcepath, "r", encoding="UTF8") as csvfile:
    csvreader = csv.reader(csvfile, delimiter = ",")
    csv_header = next(csvreader)

    #initialize variables
    total = 0
    count = 0
    prev_profit = 0
    total_change = 0
    most_increase = 0
    most_decrease = 0

    # loop through source data to calculate values to print out
    for row in csvreader:
        if count != 0:
            profit = int(row[1]) - int(prev_profit)
            total_change += profit
            # find out most and least increase
            if profit > most_increase:
                increase_month = row[0]
                most_increase = profit
            elif profit < most_decrease:
                decrease_month = row[0]
                most_decrease = profit
        
        monthyear.append(row[0])
        total += int(row[1])
        count += 1
        prev_profit = row[1]

# calculate summary data
average_change = total_change / (count - 1)
unique_month = set(monthyear)      
unique_month_count = len(unique_month)

# print Financial Analysis to result.txt file
with open(resultpath, "w") as text_file:

    print("Financial Analysis", file=text_file)
    print("------------------------------", file=text_file)

    print(f"Total Month: {unique_month_count}", file=text_file)
    print(f"Total: ${total}", file=text_file)
    print(f"Average Change: ${round(average_change,2)}", file=text_file)
    print(f"Greatest Increase in Profits: {increase_month}  (${most_increase})", file=text_file)
    print(f"Greatest Decrease in Profits: {decrease_month}  (${most_decrease})", file=text_file)

# print Financial Analysis result file content to terminal
f = open(resultpath, "r")
print(f.read())    
