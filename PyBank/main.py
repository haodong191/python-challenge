import os
import csv

csvpath = os.path.join('resources','budget_data.csv')
monthly_total = []
profit = []
monthly_change = []

with open(csvpath, encoding="utf-8") as budget_csv:
    csvreader = csv.reader(budget_csv, delimiter=',')
    csv_header =next(csvreader)
    for row in csvreader: 
        monthly_total.append(row[0])
        profit.append(int(row[1]))
    for i in range(len(monthly_total)-1):
        monthly_change.append(profit[i+1]-profit[i])
max_profit_gains = max(monthly_change)
max_profit_loses = min(monthly_change)
max_profit_month = monthly_change.index(max(monthly_change)) +1
min_profit_month = monthly_change.index(min(monthly_change)) +1

print("Financial Analysis")
print("----------------------------")
print(f"Total Months: {len(monthly_total)}")
print(f"Total: ${sum(profit)}")
print(f"Average Change: {round(sum(monthly_change)/len(monthly_change),2)}")
print(f"Greatest Increase in Profits: {monthly_total[max_profit_month]} (${(str(max_profit_gains))})")
print(f"Greatest Decrease in Profits: {monthly_total[max_profit_month]} (${(str(max_profit_loses))})")

output_path = os.path.join("analysis", "Financial_Analysis.txt")
with open (output_path, "w") as file:
    file.write("Financial Analysis")
    file.write("\n")
    file.write("----------------------------")
    file.write("\n")
    file.write(f"Total Months: {len(monthly_total)}")
    file.write("\n")
    file.write(f"Total: ${sum(profit)}")
    file.write("\n")
    file.write(f"Average Change: {round(sum(monthly_change)/len(monthly_change),2)}")
    file.write("\n")
    file.write(f"Greatest Increase in Profits: {monthly_total[max_profit_month]} (${(str(max_profit_gains))})")
    file.write("\n")
    file.write(f"Greatest Decrease in Profits: {monthly_total[min_profit_month]} (${(str(max_profit_loses))})")