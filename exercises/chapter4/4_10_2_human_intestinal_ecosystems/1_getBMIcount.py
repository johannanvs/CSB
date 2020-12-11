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

# define function
def get_BMI_count(constr_dict):
    # define dictionary
    bmi_dict = {}
    # define input file
    metadata_file = "Metadata.tab"
    # open metadata file with the DictReader module, tab delimited
    with open(metadata_file) as infile:
        # create dictionary for each header category
        csv_metadata = csv.DictReader(infile, delimiter = '\t')
        for line in csv_metadata:
            # use a Boolean to acertain that all constraints will be matched, and not just some of them
            all_matching = True
            # iterate over constraints dictionary
            for k in constr_dict:
                # if constraints does not match input, skip line
                if line[k] != constr_dict[k]:
                    all_matching = False
                    break
            if all_matching == True:
                # store BMI_group value in variable
                line_bmi = line['BMI_group']
                # add bmi group
                # if bmi group is already in dictionary, add 1 to the records
                if line_bmi in bmi_dict.keys():
                    bmi_dict[line_bmi] += 1
                # if bmi group is not in dictionary, initate it and add 1 to the records
                else:
                    bmi_dict[line_bmi] = 1
    
    print(bmi_dict)

# Call the function
get_BMI_count({"Age": "28", "Sex": "female"})
