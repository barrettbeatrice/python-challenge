#Financial Analysis
import csv
import os
 
#fetch the csv file
csv_file = os.path.join("/Users/bbjf/vu/Homework/03-python/python-challenge/PyPoll/Resources", "election_data.csv")

##VARIABLES ASSIGNED
# Initialize all a)lists and b)dictionaries as blank
# a total vote counter.
total_votes = 0

# Candidate Options and candidate votes.
candidate_options = []   #setting up a blank LIST of candidate names to be filled and appended
candidate_votes = {}     #setting up a blank DICTIONARY and keys will be candidate names and number of votes they get each

# 1: Create a county list and county votes dictionary.
county_options = []
county_votes = {}

# Initialize and Track the winning candidate, vote count and percentage
#This is a common method of election results, will later put in for loop, iterating through the candidates
winning_candidate = ""  #an empty string will be filled with a name
winning_count = 0     #will store votes for each candidate
winning_percentage = 0    #will store the percentage of votes of the winning candidate

# 2: Track the largest county and county voter turnout.
largest_county = ""  #same idea as tracking votes but this is by county
county_turnout = 0
county_percentage = 0


#now open file
with open(csv_file, newline = "") as csvfile:
    reader = csv.reader(csvfile)
     # Read the header
    header = next(reader)
    # For each row in the CSV file, read and iterate to next row
    for row in reader:
        total_votes = total_votes + 1
        #Get candidate name from each row
        candidate_name = row[2]
        #Extract the county name from each row
        county_name = row[1]
      
        #conditional if or not already in new dictionary
        if candidate_name not in candidate_options:

            # Add the candidate name to the candidate list by appending the list
            candidate_options.append(candidate_name)

            # And begin tracking that candidate's voter count, initialize at 0
            candidate_votes[candidate_name] = 0

     # Add a vote to that candidate's count, iterating by 1
        candidate_votes[candidate_name] += 1

    
    ##Now do the same conditional for county
        if county_name not in county_options:

            #Add the county to the list of counties
            county_options.append(county_name)

            #And begin tracking the county's vote count
            county_votes[county_name] = 0

        # Add a vote to that county's vote count.
        county_votes[county_name] += 1    


######Now to convert analysis to output via txt and save

# Add a variable to save the file to a path.
text_file = os.path.join("analysis", "election_results.txt")

# Save the results to our text file, writer mode
with open(csv_file, "w") as txt_file:

    ###### Print the final vote count (to terminal) and format
    election_results = (
        f"\nElection Results\n"
        f"-------------------------\n"
        f"Total Votes: {total_votes:,}\n"
        f"-------------------------\n\n"
        f"County Votes:\n")
    print(election_results, end="")

####N Now we tell what to write into the lists on text file created
    txt_file.write(election_results) 


##### Write a for loop to get the county from the county dictionary
    for county_name in county_votes:
        vote_count = county_votes.get(county_name)  #get function in our dictionary
         #Calculate the percentage of votes for the county.
        turnout_percentage = float(vote_count) / float(total_votes) * 100  #vote count totals are floating

        #Print the county results to the terminal. Dict = "County Name", "Percentage Turnout", "Total Votes in County"
        county_results = (
            f"{county_name}: {turnout_percentage:.1f}% ({vote_count:,})\n")
        print(county_results)
         #Save the county votes to a text file with writer
        txt_file.write(county_results)

        #Write an if statement to determine the winning county and get its vote count.
        if (vote_count > county_turnout):
            county_turnout = vote_count
            largest_county = county_name
            county_percentage = turnout_percentage
        
    #Print and format the county with the largest turnout to the terminal
    largest_county_summary = (
        f"\n-------------------------\n"
        f"Largest County Turnout: {largest_county}, with {county_turnout:,} votes ({county_percentage:.1f}%).\n" #needed to look this up
        f"-------------------------\n")
    print(largest_county_summary)

    #Save the county with the largest turnout to a text file
    txt_file.write(largest_county_summary)

    #Save the final candidate vote count to the text file
    for candidate_name in candidate_votes:
         # Retrieve vote count and percentage
        votes = candidate_votes.get(candidate_name)
        vote_percentage = float(votes) / float(total_votes) * 100
        candidate_results = (
            f"{candidate_name}: {vote_percentage:.1f}% ({votes:,})\n")

        # Print each candidate's voter count and percentage to the terminal
        print(candidate_results)
        #  Save the candidate results to our text file.
        txt_file.write(candidate_results)

        # Determine winning vote count, winning percentage, and candidate.
        if (votes > winning_count) and (vote_percentage > winning_percentage):
            winning_count = votes
            winning_candidate = candidate_name
            winning_percentage = vote_percentage

    # Print the winning candidate (to terminal)
    winning_candidate_summary = (
        f"-------------------------\n"
        f"Winner: {winning_candidate}\n"
        f"Winning Vote Count: {winning_count:,}\n"
        f"Winning Percentage: {winning_percentage:.1f}%\n"
        f"-------------------------\n")
    print(winning_candidate_summary)

    # Save the winning candidate's name to the text file
    txt_file.write(winning_candidate_summary)





 






  