#!/usr/bin/env python3
# coding: utf-8

# Date: 2020-12-11, Johanna von Seth

# This scripts calculates the mean population for each city.
# The script assumes your located in CSB/exercises/chapter3/3_8_1_measles_time_series/ when running it.

###########################################
## Usage: python3 3_mean_pop_per_city.py ##
###########################################

# import csv module to process csv data file
import csv

# store path to data and data file in string variable
datafile="../../../python/data/Dalziel2016_data.csv"

# create an empty dictionary
cities = {}

# open data file
with open(datafile) as infile:
    #count = 0
    # set up a dictionary reader
    reader = csv.DictReader(infile)
    for line in reader:
        #count += 1
        my_city = line["loc"]
        my_pop = line["pop"]
        # if city is not in the dictionary, add it
        if my_city not in cities:
            # first value in the key's list is the population, second is how many entries that city has had
            cities[my_city] = [0.0, 0]
            # add population value and increase the number of entries with 1
            cities[my_city][0] += float(my_pop)
            cities[my_city][1] += float(1)
        else:    
            # add population value and increase the number of entries with 1
            cities[my_city][0] += float(my_pop)
            cities[my_city][1] += float(1)
        #if count > 2:
            #break
    
for (key, val) in cities.items():
    print(key + ", Mean population: " + str(round(val[0] / val[1], 1)))
