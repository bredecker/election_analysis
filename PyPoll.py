#The data we need to retrieve:
#1. The total number of votes cast
#2. A complete list of the canidates who received votes
#3. The percentage of votes each candidate won
#4. The total number of votes each candidate won
#5. The winner of the election based on popular vote

import csv
import os
total_votes = 0
#candidate_name = 0
candidate_options = []
candidate_votes = {}
county_options = []
county_name = []
county_votes = {}
#vote_percentage = (candidate_votes / total_votes) * 100

winning_candidate = ""
winning_count = 0
winning_percentage = 0

#Assign a variable for the file to load and the path
#file_to_load = os.path.join("resources", "election_results.csv")
file_to_load = "C:\\Users\\Owner\\Desktop\\Classwork\\Mod3Python\\election_analysis\\Resources\\election_results.csv"
#Open the election results and read the file
with open(file_to_load) as election_data:

    reader = csv.reader(election_data)
    header = next(reader)
    #print(header)

    for row in reader: 
        total_votes = total_votes + 1
        candidate_name = row[2]
        county_name = row[1]

        if candidate_name not in candidate_options:
            candidate_options.append(candidate_name)
            candidate_votes[candidate_name] = 0
        candidate_votes[candidate_name] += 1

    for candidate_name in candidate_votes: 
        votes = candidate_votes[candidate_name]
        vote_percentage = float(votes) / float(total_votes) * 100
        print(f"{candidate_name} received {votes:,} votes, {vote_percentage:.1f}% of the vote.")
        

        if county_name not in county_options:
            county_options.append(county_name)
            county_votes[county_name] = 0
        county_votes[county_name] += 1 
        


        if (votes > winning_count) and (vote_percentage > winning_percentage): 
            winning_count = votes
            winning_percentage = vote_percentage
            winning_candidate = candidate_name


winning_candidate_summary = (
        f"----------------------\n"
        f"Winner: {winning_candidate}\n"
        f"Winning Vote Count: {winning_count:,}\n"
        f"Winning Percentage: {winning_percentage:.1f}%\n"
        f"----------------------\n")
print(winning_candidate_summary)
    
            

#print(winning_candidate)
#print(candidate_options)
#print(candidate_votes)
#print(county_votes)
#print(total_votes)
#print(vote_percentage)

file_to_save = os.path.join("analysis", "election_analysis.txt")

with open(file_to_save, "w") as txt_file:
    election_results = f"The results are {winning_candidate_summary}"
    txt_file.write(election_results)



#To do: Perform analysis
    print(election_data)

#Close the file. 
election_data.close()


#Create a filename variable to a direct or indirect path to the file. 

#Use the open statement to open the file as a text file.
#with open(file_to_save, "w") as txt_file: 
#Write some data to the file. 
    #txt_file.write("Hello world!")


#Close the file
#outfile.close()