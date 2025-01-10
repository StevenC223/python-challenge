# -*- coding: UTF-8 -*-
"""PyBank Script - Analyzes financial records"""
 
# Import necessary modules
import csv  # For reading CSV files
import os   # For handling file paths
 
# Files to load and output (update with correct file paths)
file_to_load = r"C:\\Users\\carls\\Desktop\\Repositories\\python-challenge\\PyBank\\Resources\\budget_data.csv"
file_to_output = r"C:\\Users\\carls\Desktop\\Repositories\\python-challenge\\PyBank\\analysis\budget_analysis.txt"

# Define variables to track the financial data
total_months = 0      
total_net = 0        
net_change_list = [] 
date_list = []       
previous_net = None  
 # Add more variables to track other necessary financial data

# Open and read the csv
with open(file_to_load) as financial_data:
        
    reader = csv.reader(financial_data)
 
    # Skip the header row 
    header = next(reader)  
    # Extract first row to avoid appending to net_change_list
    first_row = next(reader)
    total_months = 1  
    total_net = int(first_row[1])  
    previous_net = int(first_row[1])  
 
     # Track the total
    for row in reader:
        total_months += 1
 
        current_net = int(row[1])
        total_net += current_net
 
        
        net_change = current_net - previous_net
 
        date_list.append(row[0])
        net_change_list.append(net_change)
 
        previous_net = current_net
 

# Calculate the greatest increase in profits (month and amount)
average_change = sum(net_change_list) / len(net_change_list)
 
# Track the net change
greatest_increase = max(net_change_list)
greatest_decrease = min(net_change_list)
 
# Calculate the greatest decrease in losses (month and amount)
increase_date = date_list[net_change_list.index(greatest_increase)]
decrease_date = date_list[net_change_list.index(greatest_decrease)]
 
# Generate the output summary
output = (
        "\nFinancial Analysis\n"
        "-------------------------\n"
        f"Total Months: {total_months}\n"
        f"Total: ${total_net:,}\n"
        f"Average Change: ${average_change:,.2f}\n"
        f"Greatest Increase in Profits: {increase_date} (${greatest_increase:,})\n"
        f"Greatest Decrease in Profits: {decrease_date} (${greatest_decrease:,})\n"
    )
 
    # Print the output
print(output)
 
    # Write results to text file
with open(file_to_output, "w") as txt_file:
        txt_file.write(output)
 
print(f"\nResults have been written to: {file_to_output}")
