#!/usr/bin/env python
# coding: utf-8

# In[ ]:


# Singh et al. (2015) show that, when infected with a parasite, the four genetic
# lines of D. melanogaster respond by increasing the production of recombinant
# offspring (arguably, trying to produce new recombinants able to escape
# the parasite). They show that the same outcome is not achieved by artificially
# wounding the flies. The data needed to replicate the main claim (figure 2 of
# the original article) is contained in the file Singh2015_data.csv.
# Open the file, and compute the mean RecombinantFraction for each
# Drosophila Line, and InfectionStatus (W for wounded and I for infected).
# Print the results in the following form:

# Line 45 Average Recombination Rate:
# W : 0.187
# I : 0.191


# In[ ]:


# What do I have?
# A comma separated file with header
    # Read file with csv module Dictreader

# What do I want?
# mean RecombinantFraction (RecombinantFraction) for each Drosophila line (Line) and each InfectionStatus (InfectionStatus)
    # Thus, all columns included in output
    
# Lines could be stored in dictionary as keys
    # Each corresponding value is another dictionary, 
    # where InfectionStatus is key and RecombinantFraction + count is values (in a list)

###############
# PSEUDO CODE #
###############

# import csv module

# initiate necesseary variables
# line_dict = {}
# mean = 0

# with open file as f1:
    # reader = read file and automatically store headers as key
    # for each line in file:
        # if Line not in Line dictionary: 
            # intialize both line dictionary and subdictionary
            # add RecombinationFraction, count as value to InfectionStatus subdictionary
        # else if Line in line dictionary, but InfectionStatus not in subdictionary:
            # intialize subdictionary
            # add RecombinationFraction, count as value to InfectionStatus subdictionary
        # else 
            # add Recombination, count to subdictionary

# calculate mean RecombinantFraction
# for each Line in line dictionary:
    # print Line Average Recombination Rate:
    # for each Infectionstatus in infectionstatus dictionary:
        # mean = RecombinantFraction / count
        # print InfectionStatus : mean




# MY VERSION

# import csv module
import csv

dros_dict = {}

# open file as f1:
with open("../data/Singh2015_data.csv", 'r') as f1:
    # read file and automatically store headers as key
    reader = csv.DictReader(f1)
    # for each line in file:
    for row in reader:
        my_dros = row["Line"]
        my_stat = row["InfectionStatus"]
        my_recomb = float(row["RecombinantFraction"])
        # if Drosophila Line not in Line dictionary: 
        if my_dros not in dros_dict:
            # intialize Line dictionary where the key:value pairs are InfectionStatus:RecombinantFraction
            dros_dict[my_dros] = {'W' : [], 'I' : []}
        # add RecombinantFraction to InfectionStatus list
        dros_dict[my_dros][my_stat].append(my_recomb)

#print(dros_dict)            
            
# calculate mean RecombinantFraction
# for each Drosophila Line in Line dictionary:
for dros in dros_dict.keys():
    # print Line Average Recombination Rate:
    print("Line", dros, "Average Recombination Rate:")
    # for each Infectionstatus in infectionstatus dictionary:
    for (status,recomb) in dros_dict[dros].items():
        # mean = sum of RecombinantFraction entires / number of entries
        mean = round(sum(recomb) / len(recomb), 3)
        # print InfectionStatus : mean
        print(status, ":", mean)
    print("")


# HOW IT'S DONE IN THE SOLUTION:

# import csv module
import csv

my_data = {}

# open file as csvfile:
with open("../data/Singh2015_data.csv", 'r') as csvfile:
    # read file and automatically store headers as key
    reader = csv.DictReader(csvfile)
    # for each line in file:
    for row in reader:
        my_line = row["Line"]
        my_status = row["InfectionStatus"]
        my_recomb = float(row["RecombinantFraction"])
        # if Drosophila Line not in Line dictionary: 
        if my_line not in my_data:
            # intialize Line dictionary where the key:value pairs are InfectionStatus:RecombinantFraction
            my_data[my_line] = {'W' : [], 'I' : []}
        # add RecombinantFraction to InfectionStatus list
        my_data[my_line][my_status].append(my_recomb)

#my_data

for line in my_data:
    print('Line', line, 'Average Recombination Rate:')
    # extract the relevant data
    my_subset = my_data[line]
    for status in ['W', 'I']:
        print(status, ':', end = '') # to prevent new line
        my_mean = sum(my_subset[status])
        my_num_elements = len(my_subset[status])
        my_mean = my_mean / my_num_elements
        print(' ', round(my_mean, 3))
        print('') # to separate the lines
