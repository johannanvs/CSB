#!/usr/bin/env python

"""
Last updated: 2021-01-13, Johanna von Seth

Usage: python3 exercise2_most_entries_year.py

This script contains a function that returns the year with the highest number of entries in regex/bee_list.txt. The script assumes you're located in CSB/exercises/chapter5/5_9_1_bee_checklist.

"""

# import modules
import csv
import re

# store path to file and filename in variable
file="../../../regex/data/bee_list.txt"

# open file
with open(file) as f:
	csvread = csv.DictReader(f, delimiter = '\t')
	species = []
	authors = []
	for line in csvread:
		# extract species name in list
		species.append(line['Scientific Name'])
		# extract author/date string in list 
		authors.append(line['Taxon Author'])

# build a regular expression that captures authors in one group, and the year in another group
my_regex = re.compile(r'\(?([\w\s,\.\-\&]*),\s(\d{4})\)?')
#	translation:
#	\(? = line might start with '(' and it might not
#	([\w\s,\.\-\&]*) = first group corresponding to author names
# 	,\s = the characters between the two groups, will not be saved into any group
#	(\d{4}) = second group, corresponding to publication year
#	\(? = line might end with '(' and it might not


# define function that extracts all authors separately, and year
def extract_au_year(au):
	test = re.match(my_regex, au)
	authorlist = test.group(1)
	year = test.group(2)
	# split authors into a list, either by comma or pipe sign
	authorlist = re.split(', | \& ', authorlist)
	return [authorlist, year]

# create two dictionaries, one that keeps track of number of entries/year, and one that keeps track of number of entries/author
authors_dict = {}
years_dict = {}

# iterate over entries in authors list
for au in authors:
	# run function to split authors into list, and extract year
	tmp = extract_au_year(au)
	for a in tmp[0]:
		# if author already in dict, add 1
		if a in authors_dict.keys():
			authors_dict[a] += 1
		# otherwise, add author as key and 1 as value
		else:
			authors_dict[a] = 1
	# if year already in dict, add 1
	if tmp[1] in years_dict.keys():
		years_dict[tmp[1]] += 1
	# otherwise, add year as key and 1 as value
	else:
		years_dict[tmp[1]] = 1


# Get the maxmimum number for number of entries/year
max_number = max(years_dict.values())

# Get the list index of the year with the maxmimum number of entries
max_index = list(years_dict.values()).index(max_number)

# Get the year
max_year = list(years_dict.keys())[max_index]

# Print output
print("")
print("The highest number of entries per year was " + str(max_number) + ", and were entered in " + str(max_year) + ".")
print("")
