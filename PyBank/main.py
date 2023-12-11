#Financial Analysis
import csv
import os
 
#fetch the file
csv_file = os.path.join("Resources", "budget_data.csv")
#change directory to the directory of the script
os.chdir(os.path.dirname(os.path.realpath(__file__))) #tutor suggested this with dunder, another option

#now open file
with open(csv_file) as csvfile:

#create placeholder lists to fill with the data from the csv file
    months = []
    net_total = []
 
with open(csv_file, newline = "") as csvfile:
    readcsv = csv.reader(csvfile, delimiter = ',')
 
    csv_header = next(csvfile) #read the header
     
#put the data into lists by rows and use append
    for row in readcsv:
        months.append(row[0])
        net_total.append(int(row[1]))
         
    #count the number of months (the number of rows except the header)
    month_count = len(months)
     
    #set variables for loops
    a = 1
    b = 0
     
    #average change place holder
    average_change = (net_total[1]-net_total[0]) #net_total[a] - net_total[b]
     
    #place holder list for changes 
    changes = []
     
    #Calculate the month-to-month change, store them in the changes list, and update the index variables.
    for month in range(month_count-1):
        average_change = (net_total[a] - net_total[b])
        changes.append(int(average_change))
        a+=1
        b+=1
         
     
    #Calcuate the average monthly change and round it, divide by the number of months minus 1    
    av_mon_chng = round(sum(changes)/(month_count -1),2)
 
    #find the min and max change
    min_change = min(changes)
    max_change = max(changes)
 
    #return the index to find the month positions in the list
    chng_i_min = changes.index(min_change)
    chng_i_max = changes.index(max_change)
     
    #revert from index positions to find the months for the min and max changes
    min_chng_month = months[chng_i_min + 1]
    max_chng_month = months[chng_i_max + 1]
   
 
#Print the values in console, use f-strings
 
print("Financial Analysis")
print("----------------------------")
print(f"Months: {len(months)}")
print(f"Total: ${sum(net_total)}")
print(f"Average Monthly Change: {av_mon_chng}")
print(f"Greatest Increase in Profits: {max_chng_month} (${max_change})")
print(f"Greatest Decrease in Profits: {min_chng_month} (${min_change})")
 
#open and Write the output to a text file
fin_analysis = open("Financial_Analysis.txt","w")
 
fin_analysis.write("Financial Analysis\n")
fin_analysis.write("----------------------------\n")
fin_analysis.write(f"Months: {len(months)}\n")
fin_analysis.write(f"Total: ${sum(net_total)}\n")
fin_analysis.write(f"Average Monthly Change: {av_mon_chng}\n")
fin_analysis.write(f"Greatest Increase in Profits: {max_chng_month} (${max_change})\n")
fin_analysis.write(f"Greatest Decrease in Profits: {min_chng_month} (${min_change})\n")
 
  
fin_analysis.close() 