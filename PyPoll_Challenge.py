import os
import csv

# Assign a variable for the file to load and the path.
#file_to_load = "election_results.csv"
file_to_load = os.path.join("Resources", "election_results.csv")

# Create a filename variable to a direct pqth to the output file.
file_to_save = os.path.join("analysis", "election_analysis.txt")

# Associate variable with file.
election_data = open(file_to_load, 'r')

# Initialize total vote counter, candidate_options list, and candidate_votes dictionary for names, keys and values.
total_votes = 0
candidate_options = list()
county_names = list()
candidate_votes = dict()
county_votes = dict()

# Initialize winning_candidate and winning_count to hold the name and number of votes for the county with the largest turnout.
winning_candidate =""
winning_count = 0
winning_percentage = 0
largest_turnout_countynames = ""
largest_turnout_countyvotes = 0

# Open the election results, read file and print header.
with open(file_to_load) as election_data:
    file_reader = csv.reader(election_data)
    headers = next(file_reader)
    #print(headers)
    
 # Read the rows in file_reader.    
    for row in file_reader:
        #print(row)
        
   # For each row in the CSV file, add to the total vote count.     
        total_votes = total_votes + 1
   # Get the candidate name from each row.     
        candidate_name = row[2]
   # 3: Extract the county name from each row.  
        county_name = row[1]
    
# 4a: Write an if statement that checks if the candidate name doesn't match any existing candidate add it to the candidate.        
        # Add the candidate name to the candidate list, track the voter count and add vote to candidate's count.
        if candidate_name not in candidate_options:
            candidate_options.append(candidate_name)
            candidate_votes[candidate_name] = 0
        candidate_votes[candidate_name] += 1

# Write an if statement that checks if the county name does not match any existing county in the county list.        
        # Add the existing county to the list of counties, track the county's vote count and add vote to county's vote count.
        if county_name not in county_names:
            county_names.append(county_name)
            county_votes[county_name] = 0
        county_votes[county_name] += 1

# Check For loop and Conditional coding
print(candidate_options)
print(county_names)

# Save the results to our text file. -PROBLEM SECTION-
with open(file_to_save, "w") as txt_file:

    # Print the final vote count (to terminal)
    election_results = (
        f"\nElection Results\n"
        f"-------------------------\n"
        f"Total Votes: {total_votes:,}\n"
        f"-------------------------\n\n"
        f"County Votes:\n")
    print(election_results, end="")

    txt_file.write(election_results)

     # 6a: Write a for loop to get the county from the county dictionary.
    for county in county_votes:
        # 6b: Retrieve the county vote count.
        county_vote = county_votes[county]
        
        # 6c: Calculate the percentage of votes for the county.
        county_percent = float(county_vote) / float(total_votes) * 100

        # 6d: Print the county results to the terminal.
        county_results = (
            f"{county}: {county_percent:.1f}% ({county_vote:,})\n")
        print(county_results, end = "")
        
        # 6e: Save the county votes to a text file.
        txt_file.write(county_results)
       
        # 6f: Write an if statement to determine the winning county and get its vote count.
        if (county_vote > largest_turnout_countyvotes):
            largest_turnout_countyvotes = county_vote
            largest_turnout_countynames = county
            
    # 7: Print the county with the largest turnout to the terminal.
    largest_turnout_countynames = (
        f"--------------------------------\n\n"
        f"Largest County Turnout: {largest_turnout_countynames}\n"
        f"--------------------------------\n\n")
    print(largest_turnout_countynames)

    # 8: Save the county with the largest turnout to a text file.
    txt_file.write(largest_turnout_countynames)
        
    # Save the final candidate vote count to the text file.
    for candidate_name in candidate_votes:

        # Retrieve vote count and percentage
        votes = candidate_votes.get(candidate_name)
        vote_percentage = float(votes) / float(total_votes) * 100
        candidate_results = (
            f"{candidate_name}: {vote_percentage:.1f}% ({votes:,})\n")

    # Print each candidate's voter count and percentage to the terminal.
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