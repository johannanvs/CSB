#!/usr/bin/env python

"""
Jiang et al. (2013) studied assortative mating in animals. They compiled a large database, reporting the results of many experiments on mating. In particular, for several taxa they provide the value of correlation among the sizes of the mates. A positive value of r stands for assortative mating (large animals tend to mate with large animals), and a negative value for disassortative mating.
"""

# 2. You should see that fish have a positive value of r, but that this is also true for other taxa. Is the mean value of r especially high for fish? 
	# To test this, compute a p-value by repeatedly sampling 37 values of r (37 experiments on fish are reported in the database) at random, 
	# and calculating the probability of observing a higher mean value of r. 
	# To get an accurate estimate of the p-value, use 50,000 randomizations.


# import necessary modules
#import sys
import random
import statistics


## extracting data from input file ##

# store taxon of interest in variable
target_taxon = "Fish"
# define list for taxon r values
taxon_r = []
# define list for data r values
data_r = []
# define counter for the number of target taxon occurrences
target_taxon_entries = 0
# open file
with open("Jiang2013_data.csv") as infile:
	# process line by line
	for line in infile:
		# if line startwith headers or if line is blank, skip it
		if line.startswith("Scientific") or not line.strip():
			next	
		else:
			# split line into columns
			column = line.strip().split("\t")
			# store r value in variable
			current_r_value = column[3]
			# if target_taxon is in line
			if target_taxon.title() in line:
				# add one to the number of taxon occurences
				target_taxon_entries += 1
				# append r value to taxon list
				taxon_r.append(float(current_r_value))			
			else:
				# append r value to data list
				data_r.append(float(current_r_value))

## compute mean of r ##
mean_taxon_r = statistics.mean(taxon_r)

## compute p value ##
total_counts = 0.0
count_higher_mean = 0.0

for i in range(50000):
	## random sampling ##
	# shuffle list of data r values randomly and store the first number of entries corresponding to the number of taxon entries in a new list
	random_r = random.sample(data_r, target_taxon_entries)
	
	## compute average of random values ##
	# define counter variable for the number of means that are higher than the taxon mean
	mean_random_r = statistics.mean(random_r)
	# if r value is higher than the mean of taxon r
	if mean_random_r > mean_taxon_r:
		# add 1 to total number of counts
		total_counts += 1.0
		# add 1 to count number of values higher than taxon mean r
		count_higher_mean += 1.0
	else:
		# add 1 to total number of counts
		total_counts += 1.0

## compute probabilites ##
# the probability of getting a mean value higher than the taxon mean r = number of higher means / number of taxon occurences
p_value = count_higher_mean / total_counts
print(p_value)
