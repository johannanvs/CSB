#!/usr/bin/env python3
# coding: utf-8

# Date: 2020-12-11, Johanna von Seth

# This scripts computes the mean recombinant fraction for each Drosophila line and infection status.
# The script assumes your located in CSB/exercises/chapter3/3_8_2_red_queen_in_fruit_flies/ when running it.

#################################################
## Usage: python3 mean_recombinant_fraction.py ##
#################################################

# import csv module to process csv data file
import csv

# store path to data and data file in string variable
datafile="../../../python/data/Singh2015_data.csv"

# initiate a dictionary for drosophila lines
dros_dict = {}

# open file as f1:
with open(datafile, 'r') as f1:
    # read file and automatically store headers as key
    reader = csv.DictReader(f1)
    # for each line in file:
    for row in reader:
        my_dros = row["Line"]
        my_stat = row["InfectionStatus"]
        my_recomb = float(row["RecombinantFraction"])
        # if Drosophila Line not in drosophila dictionary: 
        if my_dros not in dros_dict:
            # intialize drososphila dictionary where the key:value pairs are InfectionStatus:RecombinantFraction
            dros_dict[my_dros] = {'W' : [], 'I' : []}
        # add RecombinantFraction to InfectionStatus list
        dros_dict[my_dros][my_stat].append(my_recomb)
           
            
# calculate mean RecombinantFraction
# for each Drosophila Line in drosophila dictionary:
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

