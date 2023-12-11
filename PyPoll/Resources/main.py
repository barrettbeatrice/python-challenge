#Financial Analysis
import csv
import os
 
#fetch the file
csv_file = os.path.join("Users/bbjf/vu/Homework/03-python/python-challenge/PyPoll/Resources", "election_data.csv")
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