#!/usr/bin/env python

""" 
Last updated: 2021-01-07, Johanna von Seth

Usage: python3 exercise1_getBMIcount.py

Note! The wanted group of records should be entered at the last line of this script.

This script takes as input a dictionary of constraints (i.e., a specific group of records) from the Metadata.tab file in Lahti et al. (2014) and returns a dictionary tabulating the BMI group for all the records matching the constraints. The script assumes you're located in CSB/exercises/chapter4/4_10_2_human_intestinal_ecosystems/. 
"""

# import required modules
import csv

# define function
def get_BMI_count(constr_dict):
    # define dictionary
    bmi_dict = {}
    # define input file
    metadata_file = "../../../good_code/data/Lahti2014/Metadata.tab"
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

