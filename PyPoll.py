# The data we need to retrieve.
# 1. The total number of votes cast
# 2. A complete list of canidates who received cotes
# 3. The percentage of votes each candidate won
# 4. The total number of votes each candidate won
# 5. The winner of the election based on popular vote


import datetime as dt
import os
import csv

now = dt.datetime.now()

print(f'The time right now {now}')

file_to_load = os.path.join("Resources", "election_results.csv")

with open(file_to_load) as election_data:
    print(election_data)