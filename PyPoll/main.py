# Modules
import os
import csv

election_csv = os.path.join("Resources", "election_data.csv")

# Set existing lists
ballot_id = []
county = []
candidate = []

# Create variables to store data
candidates_votes = {}
candidates_list = []
votes_total = []
total_percent = []
winner_candidate = " "

# Set variables
total_votes = 0
winner_votes = 0

# Open and read csvfile:
with open(election_csv) as csvfile:
    csvreader = csv.reader(csvfile, delimiter =',')

    # Read the header
    csv_header = next(csvfile)

    # Read through each row of the data
    for row in csvreader:

        # Get the rows list data
        ballot_id.append(row[0])
        county.append(row[1])
        candidate.append(row[2])

        # Calulate total number of votes
        total_votes = len(ballot_id)

        # Set variable
        candidate_name = row[2]

        # Get the candidate name for each row
        if candidate_name in candidates_list:
            candidates_votes[candidate_name] = candidates_votes[candidate_name] + 1
        else:
            candidates_list.append(candidate_name)
            candidates_votes[candidate_name] = 1


    # Read through each candidates row of the data
    for candidate_name, votes in candidates_votes.items():
        
        # Get total number of votes
        votes_total.append(votes)

        # Calculate total percentage of votes and add to list of data
        votes_percent = round((votes / total_votes * 100), 3)
        total_percent.append(votes_percent)

        # Get the winners information
        if votes > winner_votes:
            
            # Track winner candidate votes
            winner_votes = votes

            # Track winner candidate
            winner_candidate = candidate_name

    # Create zipped list to organize variables
    zipped_list = list(zip(candidates_list, total_percent, votes_total))


# Set variable for output file
output_file = os.path.join(".", "Analysis", "Analysis_PyPoll.txt")

# Export to the output file
with open(output_file, "w", newline='') as txtfile:
        
    # Print the output
    output = (
        f"Election Results\n"
        f"-------------------------\n"
        f"Total Votes: {total_votes}\n"
        f"-------------------------\n"
        f"{zipped_list[0][0]}: {zipped_list[0][1]}% ({zipped_list[0][2]})\n"
        f"{zipped_list[1][0]}: {zipped_list[1][1]}% ({zipped_list[1][2]})\n"
        f"{zipped_list[2][0]}: {zipped_list[2][1]}% ({zipped_list[2][2]})\n"
        f"-------------------------\n"
        f"Winner: {winner_candidate}\n"
        f"-------------------------\n"
    )
    
    print(output)

    # Export to Analysis text file
    txtfile.write(output)    









        
