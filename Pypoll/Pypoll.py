import csv
import os
from tqdm import tqdm
from collections import Counter
from operator import itemgetter  

all_candidates = {} #dictionary of candidates who received votes

file_path= os.path.join("Resources", "election_data.csv") #open file for reading
of = open("PypollHW3.txt", "w+")    #creaate file to write results

with open(file_path, "r") as f:
    reader = csv.reader(f)
    next(reader)
    total_votes = 0

    for row in tqdm(reader):                    #add and store total votes
        candidate = row[2]
        total_votes = total_votes +1

        if candidate in all_candidates:
            all_candidates[candidate] += 1
        else:
            all_candidates[candidate] = 1
        
print(" ")                                                                                  #print results
print(f"Election Results")
print(f"_" * 25)
print(" ")    
print(f"Total Votes: {total_votes}")
print(f"_" * 25)
print("")

for cand, votes in sorted(all_candidates.items(), key = itemgetter(1), reverse = True):     #sort dictionary in descending
    percent_of_votes = "{:.3f}".format(votes / total_votes * 100)                           #value order & calculate %age votes
    print(f"{cand} {percent_of_votes}% ({votes})")

print(f"_" * 25)
print(" ")
winning_cand = max(all_candidates, key=all_candidates.get)
print(f"Winner: {winning_cand}")
print(f"_" * 25)

of.write("Election Results\n")                                                              #write results report
of.write("_" * 25 + "\n\n")
of.write("Total Votes: " + str(total_votes) + "\n")
of.write("_" * 25 + "\n\n")

for cand, votes in sorted(all_candidates.items(), key = itemgetter(1), reverse = True):
    percent_of_votes = "{:.3f}".format(votes / total_votes * 100)
    of.write(str(cand) + " " + str(percent_of_votes) + "%  (" + str(votes) + ")" + "\n")

of.write("_" * 25 + "\n\n")
of.write("Winner: " + str(winning_cand) + "\n")
of.write("_" * 25 + "\n")
of.close






