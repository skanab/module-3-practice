import os
import csv

#Setup the files we want to read and write to.
file_to_load = os.path.join("Resources", "election_results.csv")
file_to_save = os.path.join("Analysis", "election_analysis.txt")

#Read File
with open(file_to_load) as election_data:
    file_reader = csv.reader(election_data)

    headers = next(file_reader)
    print(headers)
    # for row in file_reader:
    #     print(row)

#Write File
with open(file_to_save, 'w') as election_analysis:
    election_analysis.write("Hello World!")

