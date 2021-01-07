#!/usr/bin/env python

"""
Last updated: 2021-01-07, Johanna von Seth

Usage: python3 exercise3_getAbundanceByBMIAllGenera.py 

This script contains a function that returns the average abundance (in logarithm base 10) of all genera for each BMI group in a specified subpopulation at Time = 0. The script assumes you're located in CSB/exercises/chapter4/4_10_2_human_intestinal_ecosystems/.
"""

def get_all_genera():
    # open hitchip file to get all genera:
    with open("../../../good_code/data/Lahti2014/HITChip.tab") as infile:
        headers = infile.readline().strip()
        # start from 1 since the first header is sample ID
        genera = headers.split('\t')[1:]
    return genera

###################################################################################################

# Abundance function from exercise 2

# import required modules
import csv
import math

def get_abundance_by_BMI(metadata_file, constr_dict, hitchip_file, target_genus):
    # define metadata dictionary
    metadata_dict = {}
    with open(metadata_file) as infile1:
        # store headers as keys
        metadata = csv.DictReader(infile1, delimiter = '\t')
        # for each line, check that all constraints match
        for line in metadata:
            # use a Boolean to acertain that all constraints will be matched, and not just some of them
            all_matching = True
            # iterate over constraints dictionary
            for c in constr_dict:
            # if at least one doesn't match, skip line
                if line[c] != constr_dict[c]:
                    all_matching = False
                    break
            # if all match
            if all_matching == True:
                line_bmi = line['BMI_group']
                line_id = line['SampleID']
                # store bmi group as key and sample ID as value in list
                if line_bmi in metadata_dict.keys():
                    metadata_dict[line_bmi] += [line_id]
                else:
                    metadata_dict[line_bmi] = [line_id]
            
    # define hitchip dictionary
    hitchip_dict = {}
    with open(hitchip_file) as infile2:
        # store headers as key, i.e. sample ID and the genus names
        hitchipdata = csv.DictReader(infile2, delimiter = '\t')
        for line in hitchipdata:
            line_id = line['SampleID']
            line_abundance = str(line[target_genus])
            for bmi in metadata_dict.keys(): 
                # if sample ID from metadata dictionary match line sample ID
                if line_id in metadata_dict[bmi]:
                    # store bmi group of sample ID as key in hitchip dictionary
                    # store bacterial abundance in list of that key
                    if bmi in hitchip_dict.keys():
                        hitchip_dict[bmi] += [line_abundance]
                    else:
                        hitchip_dict[bmi] = [line_abundance]

    ## Count number of entries per BMI group, and calculate the average abundance of bacterium ##
    # Define average abundance dictionary
    average_abundance = {}
    for bmi,abundance in hitchip_dict.items():
        total_count = 0.0
        total_abundance = 0.0
        # iterate over abundance entries for each bmi group
        for a in abundance:
            total_count += 1.0
            total_abundance += float(a)
        # calculate average abundance in logarithm base 10
        average_abundance[bmi] = round(math.log10(total_abundance / total_count), 2)

    ## Print final output ##
    print("")
    print("---------------------------------------------")
    print("Abundance of", target_genus)
    print("In subpopulation:")
    print("---------------------------------------------")
    print("Nationality -> ", constr_dict["Nationality"])
    print("Time ->", constr_dict["Time"])
    print("")
    print("---------------------------------------------")
    for bmi,abundance in average_abundance.items():
        print(abundance, "\t", bmi)
    print("---------------------------------------------")
    print("")

####################################################################################################

# Call function for each genera
for g in get_all_genera():
    get_abundance_by_BMI("../../../good_code/data/Lahti2014/Metadata.tab", {"Time": "0", "Nationality": "US"}, "../../../good_code/data/Lahti2014/HITChip.tab", g)