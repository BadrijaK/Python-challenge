from cgitb import text
from distutils import text_file
import os
import csv
import math

#Finding filepath of csv file
filepath = os.path.join(".", "Resources", "budget_data.csv")


months = []
profits = []
dates = []
greatestincrease = -math.inf 
greatestdecrease = math.inf

#Openeing csv to be read
with open(filepath) as csv_file:
    csv_reader = csv.DictReader(csv_file, delimiter=",")

#Looping through data 
    for row in csv_reader:
        months.append(row['Date'])
        profits.append(int(row['Profit/Losses']))

#Calculating length of all the months and the net total amount over entire period         
totalmonth = len(months)
totalprofit = sum(profits)

#Looping through data to calculate the average of the changes in profits/losses
totalProfitChanges = 0
for i in range(1, len(profits)):
    previousProfits = profits[i-1]
    currentProfits = profits[i]
    profitChange = currentProfits - previousProfits 
    totalProfitChanges = totalProfitChanges + profitChange
    currentDate = months[i]
    
#Greatest increase and decrease from the profit changes    
    if profitChange > greatestincrease:
        greatestincrease = profitChange
        max_date = currentDate
    if profitChange < greatestdecrease:
        greatestdecrease = profitChange
        min_date = current[Date]
average = round(totalProfitChanges / (totalmonth -1),2)

#Print final analysis report 
print("Financial Analysis")
print("----------------------")
print(f"Total Months: {totalmonth}")
print(f"Total: ${totalprofit}")
print(f"Average change: ${average}")
print(f'Greatest Increase in Profits: {max_date} ({greatestincrease})') 
print(f'Greatest Decrease in Profits: {min_date} ({greatestdecrease})')

writerpath = os.path.join(".", "Resources", "results.txt")

with open(writerpath, "w") as text:
    text.write("Financial Analysis\n")
    text.write("----------------------\n")
    text.write(f"Total Months: {totalmonth}\n")
    text.write(f"Total: ${totalprofit}\n")
    text.write(f"Average change: ${average}\n")
    text.write(f'Greatest Increase in Profits: {max_date} ({greatestincrease})\n') 
    text.write(f'Greatest Decrease in Profits: {min_date} ({greatestdecrease})\n')



csv_file.close()


