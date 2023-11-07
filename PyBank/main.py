# Modules
import os
import csv
import statistics as st

budget_csv = os.path.join("Resources", "budget_data.csv")   

# Set existing lists
date = []
pol = []

# Create lists to store data
total_months = []
net_total = []
average_change = []
change_pol = []
greatest_increase = []
greatest_decrease = []

# Set variables
total_months = 0
net_total = 0
change = 0

# Open and read csvfile:
with open(budget_csv) as csvfile:
    csvreader = csv.reader(csvfile, delimiter =',')

    # Read the header
    csv_header = next(csvfile)

    # Read through each row of the data
    for row in csvreader:

        # Get the rows list data
        date.append(row[0])
        pol.append(row[1])

        # Calculate total number of months
        total_months = len(date)

        # Calculate net total for Profits/Losses
        net_total = net_total + int(row[1])

    # Calculate average changes in Profits/Losses
    for change in range(len(pol) - 1):
        value_pol = int(pol[change + 1]) - int(pol[change])
        change_pol.append(value_pol)
    average_change = sum(change_pol)/len(change_pol)

    # Calculate greatest increase in Profits (date and amount)
    greatest_increase = max(change_pol)
    greatest_increase_value = change_pol.index(greatest_increase)
    greatest_increase_date = date[greatest_increase_value + 1]

    # Calculate greatest decrease in Profits (date and amount)
    greatest_decrease = min(change_pol)
    greatest_decrease_value = change_pol.index(greatest_decrease)
    greatest_decrease_date = date[greatest_decrease_value + 1]


# Set variable for output file
output_file = os.path.join("Analysis_PyBank.txt")

# Export to the output file
with open(output_file, "w", newline='') as txtfile:
    
    # Print the output
    output = (
        f"Financial Analysis\n"
        f"----------------------------\n"
        f"Total Months: {total_months}\n"
        f"Total: ${net_total}\n"
        f"Average Change: ${average_change:.2f}\n"
        f"Greatest Increase in Profits: {greatest_increase_date} (${str(greatest_increase)})\n"
        f"Greatest Decrease in Profits: {greatest_decrease_date} (${str(greatest_decrease)})\n"
    )

    print(output)

    # Export to Analysis text file
    txtfile.write(output)