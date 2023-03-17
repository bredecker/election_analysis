#The data we need to retrieve:
#1. The total number of votes cast
#2. A complete list of the canidates who received votes
#3. The percentage of votes each candidate won
#4. The total number of votes each candidate won
#5. The winner of the election based on popular vote

import csv
import os

#Assign a variable for the file to load and the path
#file_to_load = os.path.join("resources", "election_results.csv")
file_to_load = "C:\\Users\\Owner\\Desktop\\Classwork\\Mod3Python\\election_analysis\\Resources\\election_results.csv"
file_to_save = os.path.join("analysis", "election_analysis.txt")


candidate_name = []

candidate_options = []
candidate_votes = {}

total_votes = 0

county_name = []
county_list = []
county_votes = {}
#total_county_votes = 0

winning_county = ""
greatest_countyvotes = 0
greatest_countypercentage = 0

winning_candidate = ""
winning_count = 0
winning_percentage = 0


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

        
        if county_name not in county_list:
            county_list.append(county_name)
            county_votes[county_name] = 0
        county_votes[county_name] += 1
        

with open(file_to_save, "w") as txt_file:
    election_results = (
            f"\nElection Results\n"
            f"--------------------\n"
            f"Total Votes: {total_votes:,}\n"
            f"--------------------\n")
    print(election_results, end="")
    txt_file.write(election_results)


    for county_name in county_list: 
            county_votecount = county_votes[county_name]
            county_votepercentage = float(county_votecount) / float(total_votes) * 100

            if (county_votecount > greatest_countyvotes) and (county_votepercentage > greatest_countypercentage):
                winning_countycount = county_votecount
                greatest_countyvotepercentage = county_votepercentage
                greatest_countyturnout = county_name

                county_results = (
                  f"{county_name} received {county_votecount} votes, {county_votepercentage:.1f}% of the vote.\n")
            print(county_results)
            txt_file.write(county_results)

    county_voting_summary = (
                    f"------------------------\n" 
                    f"Largest County Turnout: {greatest_countyturnout}\n"
                    f"------------------------\n")
    print(county_voting_summary)
    txt_file.write(county_voting_summary)



    for candidate_name in candidate_votes: 
            votes = candidate_votes[candidate_name]
            candidate_votepercent = float(votes) / float(total_votes) * 100
            
            candidate_results = (
                 f"{candidate_name} received {votes:,} votes, {candidate_votepercent:.1f}% of popular vote.\n")
            print(candidate_results)
            txt_file.write(candidate_results)


            if (votes > winning_count) and (candidate_votepercent > winning_percentage): 
                    winning_votecount = votes
                    winning_percentage = candidate_votepercent
                    winning_candidate = candidate_name


    winning_candidate_summary = (
                f"----------------------\n"
                f"Winner: {winning_candidate}\n"
                f"Winning Vote Count: {winning_votecount:,}\n"
                f"Winning Percentage: {winning_percentage:.1f}%\n"
                f"----------------------\n")
    print(winning_candidate_summary)
    txt_file.write(winning_candidate_summary)
            
#To do: Perform analysis
print(election_data)

#Close the file. 
election_data.close()
