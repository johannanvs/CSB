#!/usr/bin/env python

"""
Jiang et al. (2013) studied assortative mating in animals. They compiled a large database, reporting the results of many experiments on mating. In particular, for several taxa they provide the value of correlation among the sizes of the mates. A positive value of r stands for assortative mating (large animals tend to mate with large animals), and a negative value for disassortative mating.
"""

# 3. Repeat the procedure for all taxa.


# import previous custom function
import pValue

# define list with taxon names
taxon_names = []

# open Jiang file
with open("Jiang2013_data.csv") as infile:
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
	pValue.calculate_p_value("Jiang2013_data.csv", target_taxon=t, number_rand=50000)
	