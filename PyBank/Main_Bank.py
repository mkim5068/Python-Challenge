import os
import csv

budget_data = os.path.join("budget_data.csv")

with open(budget_data, "r", newline="") as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")
    csv_header = next(csvfile)

    profit = []
    months = []
    budget_change = []

    for rows in csvreader:
        profit.append(int(rows[1]))
        months.append((rows[0]))
    
    for x in range(1, len(profit)):
        budget_change.append(profit[x]-profit[x-1])
        
    budget_change_average = sum(budget_change) / len(budget_change)
    budget_change_average = round(budget_change_average,2)

    greatest_increase = max(budget_change)
    greatest_increase_date = str(months[budget_change.index(max(budget_change))+1])
    greatest_decrease = min(budget_change)
    greatest_decrease_date = str(months[budget_change.index(min(budget_change))+1])

    print("Financial Analysis")
    print("---------------------------------------------------------")
    print(f"Total months: {len(months)}")
    print(f"Total: ${sum(profit)}")
    print(f"Average Change: ${budget_change_average}")
    print(f"Greatest Increase in Profits: {greatest_increase_date} (${greatest_increase})")
    print(f"Greatest Decrease in Profits: {greatest_decrease_date} (${greatest_decrease})")

    file = open("output.txt", "w")
    file.write("Financial Analysis" + "\n")
    file.write("...................................................................................." + "\n")
    file.write(f"Total months: {len(months)}" + "\n")
    file.write(f"Total: ${sum(profit)}" + "\n")
    file.write(f"Average Change: ${budget_change_average}" + "\n")
    file.write(f"Greatest Increase in Profits: {greatest_increase_date} (${greatest_increase})" + "\n")
    file.write(f"Greatest Decrease in Profits: {greatest_decrease_date} (${greatest_decrease})" + "\n")
    file.close()

