#Financial Analysis of Budget Data
import csv #Import csv module

with open ('budget_data.csv') as csvfile: #get csv file and read it

    csvreader=csv.reader(csvfile, delimiter=',') #Specify delimiter and variable
    header=next(csvreader) #Read the header row first



#need total number of months
#net total amount of profits/losses over period
#Prepare variables
    months=[] #Generate list named "months" for the "Date" column
    prolosses=[] #Generate list named "prolosses" for the "Profit/Losses" column

 #Read in each row of data after the header and write data into lists
    for row in csvreader:
        month=row[0] #Assign column 0 as month (index begins at 0)
        proloss=row[1] #Assign column 1 as proloss
        months.append(month) #Use append function, add next line to list months
        prolosses.append(proloss) #and list prolosses
    m_count = len(months) #Count the total of months in the "Date" column
    
    print(m_count)
        #run and shows 86 months
    
    
