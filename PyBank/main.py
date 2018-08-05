#Your task is to create a Python script that analyzes the records to calculate each of the following:
	
import os
import csv

csvpath = os.path.join('Resources', 'budget_data.csv')
output_file = "main.txt"


	#The total number of months included in the dataset

#Variables
month_count=0
total_revenue=0
loss_date="unknown"
gain_date="unknown"
avg_change=0
current_month=0
prior_month=0
large_gain=0
large_loss=0
different=[]
total_avg_change=0

#The total net amount of "Profit/Losses" over the entire period

with open(csvpath) as budget_data:
	csvreader = csv.DictReader(budget_data, delimiter=',')
	for row in csvreader:
		
		total_revenue = total_revenue+ int(row["Profit/Losses"])

		month_count = month_count + 1
#calculating change in current month rec
		current_month=int(row["Profit/Losses"])
		change=current_month - prior_month
		different.append(change)

		prior_month=current_month

# The greatest increase in profits (date and amount) over the entire period
		if change > large_gain:
			large_gain = change
			gain_date = row["Date"]  	

# The greatest decrease in losses (date and amount) over the entire period

		if change < large_loss:
			large_loss = change
			loss_date = row["Date"]

  	#The average change in "Profit/Losses" between months over the entire period

avg_change= sum(different[1:])/(len(different)-1) 



#output
output = (
	f"Financial Analyses \n"
	f"------------------------------ \n"
	f"Month_Count: {month_count} \n"
	f"Total_Revenue: ${total_revenue} \n"
	f"Average Revenue Change: ${avg_change} \n"
	f"Greatest Increase in Revenue: {gain_date} ${large_gain} \n"
	f"Greatest Decrease in Revenue: {loss_date} ${large_loss} \n")


#print statement
print(output)

#export to text file
with open(output_file, "w") as txt_file:
	txt_file.write(output)





 	