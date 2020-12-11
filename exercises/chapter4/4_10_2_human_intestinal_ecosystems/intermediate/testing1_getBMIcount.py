#!/usr/bin/env python

# Lahti et al. (2014) studied the microbial communities living in the intestines of 1000 individuals. They found that bacterial strains tend to be either absent or abundant, and posit that this would reflect bistability in these bacterial assemblages. The data used in this study are contained in the directory good_code/data/Lahti2014. The directory contains:
# Metadata.tab: characterizing each of the 1006 human records
# HITChip.tab: containing HITChip signal estimates of microbial abundance
# README: a description of the data by the study authors.

# 1. Write a function that takes as input a dictionary of constraints (i.e., selecting a specific group of records) and returns a dictionary tabulating the BMI group for all the records matching the constraints. For example, calling:

#       get_BMI_count({"Age": "28", "Sex": "female"})

# should return

#       {'NA': 3, 'lean': 8, 'overweight': 2, 'underweight': 1}

# import required modules
import csv
import sys

# define input dictionary, for testing purposes
dict_constraints = {'Age': '28', 'Sex': 'female'}

# define output dictionary
bmi_dict = {}

# testing function
with open('Metadata.tab') as f:
    csvr = csv.DictReader(f, delimiter = '\t')
    for i, row in enumerate(csvr):        
        # check that all conditions are met
        matching = True
        for e in dict_constraints:
            if row[e] != dict_constraints[e]:
                # The constraint is not met. Move to the next record
                matching = False
                break
                print("in row", i, "the key", e,"in data does not match", e, "in constraints")
            if row[e] == dict_constraints[e]:
                print("in row", i, "the key", e, "in data matches", e, "in constraints")
        if i > 20:
            break