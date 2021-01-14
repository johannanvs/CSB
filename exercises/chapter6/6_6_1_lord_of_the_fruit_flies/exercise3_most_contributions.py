#!/usr/bin/env python

"""
Last updated: 2021-01-14, Johanna von Seth

Usage: python3 exercise3_most_contributions.py

This script identifies the five authors that published most contributions on D. virilis. The script assumes you're located in CSB/exercises/chapter6/6_6_1_lord_of_the_fruit_flies.

"""
# import modules
import re
import os

# create dictionary for authors
auth_dict = {}

# 3. Count the number of contributions per author.

# open file and read the whole file at once
with open("d_virilis_abstracts.txt", "r") as datafile:
    # capture 'AU' field
    for line in datafile:
        if re.match(r"AU ", line):
            # split line so that author name is separated
            newline = line.split("-", 1)
            author = newline[1].strip()
            # if author is already in the dictionary, add it
            if author in auth_dict:
                auth_dict[author] += 1
            # otherwise, add it as key
            else:   
                auth_dict[author] = 1

# sort the dictionary according to value size
print("These are the authors with the highest number of contributions:")
print("")
for author in sorted(auth_dict, key = auth_dict.get, reverse = True)[:5]:
    print(author, ":", auth_dict[author])


# delete file created by first script
os.remove("d_virilis_abstracts.txt")
print("")
print("Exercise finished!\n")
print("The output file 'd_virilis_abstracts.txt' from exercise1_2_pubmed_records.py has been deleted.")