#!/usr/bin/env python

"""
Jiang et al. (2013) studied assortative mating in animals. They compiled a large database, reporting the results of many experiments on mating. In particular, for several taxa they provide the value of correlation among the sizes of the mates. A positive value of r stands for assortative mating (large animals tend to mate with large animals), and a negative value for disassortative mating.
"""

# 1. You can find the data in good_code/data/Jiang2013_data.csv. Write a function that takes as input the desired Taxon and returns the mean value of r.


# import necessary modules
import sys
import statistics

# create and define function to compute mean r of input taxon
def compute_mean_r(file, input_taxon):
	
	## extracting data from input file ##

	# define list for r values
	mating = []

	# open file
	with open(file) as inputfile:
		# process line by line
		for line in inputfile:
			# skip blank lines
			if line.strip():
				# split line into columns
				column = line.strip().split("\t")
				# store line taxon in a variable, make lowercase
				line_taxon = column[1].lower()
				# store line r in a variable
				line_mating = column[3]
				# if lowercase input taxon = lowecase line taxon
				if input_taxon.lower() == line_taxon:
					# add line r value to the list
					mating.append(float(line_mating))

	## calculate mean value of r for input taxon ##

	mean_r = statistics.mean(mating)
	print("The mating mean of taxon", input_taxon, "is:", round(mean_r, 3))
	if mean_r < 0:
		print("Since the mean value of r is negative, this taxon mostly consist of species with disassortative mating.")
	else:
		print("Since the mean value of r is positive, this taxon mostly consist of species with assortative mating.")



if __name__ == "__main__":
	# read the arguments on the command line 
	# (they are strings by default)
	user_file = sys.argv[1]
	user_taxon = sys.argv[2]
	# call the function
	compute_mean_r(user_file, user_taxon)

