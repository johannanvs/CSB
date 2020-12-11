#!/usr/bin/env python3
# coding: utf-8

# Date: 2020-12-11, Johanna von Seth

# This scripts extracts the names of all the cities in the database (one entry per city).
# The script assumes your located in CSB/exercises/chapter3/3_8_1_measles_time_series/ when running it.

####################################
## Usage: python3 1_city_names.py ##
####################################

# import csv module to process csv data file
import csv

# store path to data and data file in string variable
datafile="../../../python/data/Dalziel2016_data.csv"

# create empty list for the storing of the cities
cities = []

# open file
with open(datafile) as infile:
    # read file and convert each row to a dictionary, where the headers in the first line are automatically saved as the keys
    reader = csv.DictReader(infile)
    for row in reader:
        # only consider new entries
        if row["loc"] in cities:
            continue
        else:
            # add new city to the list
            cities.append(row["loc"])

# print all unique city entries    
print(cities)