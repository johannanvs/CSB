#!/usr/bin/env python3
# coding: utf-8

# Date: 2020-12-11, Johanna von Seth

# This scripts extracts the names of all the cities and reports the number of records for each city.
# The script assumes your located in CSB/exercises/chapter3/3_8_1_measles_time_series/ when running it.

##########################################
## Usage: python3 2_records_per_city.py ##
##########################################

# import csv module to process csv data file
import csv

# store path to data and data file in string variable
datafile="../../../python/data/Dalziel2016_data.csv"

# create an empty list
#cities_list = []

# create an empty dictionary
cities_dict = {}

# open file
with open(datafile) as infile:
    count = 0
    # read file and convert each row to a dictionary, where the headers in the first line are automatically saved as the keys
    reader = csv.DictReader(infile)
    for row in reader:
        # if the city is in the dictionary, add 1 to it's counts (value in dict)
        if row["loc"] in cities_dict.keys():
            cities_dict[row["loc"]] += 1
        else:
            # if the city is not in the dictionary, add it
            cities_dict[row["loc"]] = 1


for city, count in cities_dict.items():
	print(city)
	print(count)