import os
import csv

#Setup the files we want to read and write to.
file_to_load = os.path.join("Resources", "election_results.csv")
file_to_save = os.path.join("Analysis", "election_analysis.txt")

#Read File
with open(file_to_load) as election_data:
    print(election_data)

#Write File
with open(file_to_save, 'w') as election_analysis:
    election_analysis.write("Hello World!")

