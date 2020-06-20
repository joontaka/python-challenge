# import packages
import os
import csv

# set file path for source and output files
sourcepath = os.path.join("Resources", "election_data.csv")
resultpath = os.path.join("analysis", "result.txt")

# open and read csv source file
with open(sourcepath, "r", encoding = "utf-8") as csvfile:
    csv_header = next(csvfile)
    csvreader = csv.reader(csvfile, delimiter=",")

    # summerize candidate and vote count into a dictionary 
    # count total vote
    candidates = {}
    vote_count = 0
   
    # loop through csv data read
    # if candidate exists in the dictionary, update vote count 
    # if candidate does not exist in the dictionay, add 
    for row in csvreader:
        if row[2] in candidates:
            candidates[row[2]] += 1
        else: 
            candidates[row[2]] = 1
    
        vote_count += 1

    # print header and Total Votes
    with open(resultpath, "w") as text_file:
        # print header for the result
        print ("Election Results", file=text_file)
        print ("----------------------------", file=text_file)
        print (f"Total Votes: {vote_count}", file=text_file)
        print ("----------------------------", file=text_file)

        # initialize variable for the loop
        winner_vote = 0

        # print each candidate,caliculated vote %, vote count and find winner
        for key,values in candidates.items():
            if values > winner_vote:
                winner = key
                winner_vote = values
            # format vote_percent to 9.999% as the HW example
            vote_percent = "{:.3%}".format(values / vote_count)
            print(f"{key}: {vote_percent} ({values})", file=text_file)

        # print the winner
        print ("----------------------------", file=text_file)
        print(f"Winner: {winner}", file=text_file)    
        print ("----------------------------", file=text_file)

    # print the result.txt file to terminal
    f = open(resultpath, "r")
    print(f.read())