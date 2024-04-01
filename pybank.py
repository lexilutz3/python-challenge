# import os
import csv

# bank_csv = os.path.join("..", "Resources", "census_starter.csv")

total_months = 0
total = 0
changes = []
previous_profit_loss = None
greatest_increase = 0
greatest_decrease = 0
greatest_increase_date = None
greatest_decrease_date = None

with open("budget_data.csv", "r") as budget_data:
    budat = csv.reader(budget_data)

    next(budat)

    for row in budat:
        total_months += 1

        
        profit_loss = int(row[1])
        
        
        total += profit_loss

       
        if previous_profit_loss is not None:
            change = profit_loss - previous_profit_loss
            changes.append(change)

           
            if change > greatest_increase:
                greatest_increase = change
                greatest_increase_date = row[0]
            elif change < greatest_decrease:
                greatest_decrease = change
                greatest_decrease_date = row[0]

        
        previous_profit_loss = profit_loss


average_change = sum(changes) / len(changes)


print("Financial Analysis")
print("------------------")
print(f"Total Months: {total_months}")
print(f"Total: ${total}")
print(f"Average Change: ${average_change:.2f}")
print(f"Greatest Increase in Profits: {greatest_increase_date} (${greatest_increase})")
print(f"Greatest Decrease in Profits: {greatest_decrease_date} (${greatest_decrease})")

with open("financial_analysis.txt", "w") as outfile:
    outfile.write("Financial Analysis\n")
    outfile.write("------------------\n")
    outfile.write(f"Total Months: {total_months}\n")
    outfile.write(f"Total: ${total}\n")
    outfile.write(f"Average Change: ${average_change:.2f}\n")
    outfile.write(f"Greatest Increase in Profits: {greatest_increase_date} (${greatest_increase})\n")
    outfile.write(f"Greatest Decrease in Profits: {greatest_decrease_date} (${greatest_decrease})\n")
