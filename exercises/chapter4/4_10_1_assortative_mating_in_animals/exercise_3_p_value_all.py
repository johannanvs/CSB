#!/usr/bin/env python

"""
Calculate the p value of r for all taxons in CSB/good_code/data/Jiang2013_data.csv.

Usage: python3 3_p_value_all.py
"""

# import previous custom function
import 2_p_value

# store filename in variable
datafile="../../../good_code/data/Jiang2013_data.csv"

# define list with taxon names
taxon_names = []

# open Jiang file
with open(datafile) as infile:
	# read line by line
	for line in infile:
		# if line is not blank
		if line.strip() and not line.startswith("Scientific"):
			column = line.strip().split("\t")
			line_taxon = column[1]
			# if taxon name in line is not in taxon names list, add it to the list
			if line_taxon not in taxon_names:
				taxon_names.append(line_taxon)

# for each taxon in taxon names list
for t in taxon_names:
	# do previous function
	pValue.calculate_p_value(datafile, target_taxon=t, number_rand=50000)
	