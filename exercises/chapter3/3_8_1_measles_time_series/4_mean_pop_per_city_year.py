#!/usr/bin/env python3
# coding: utf-8

# Date: 2020-12-11, Johanna von Seth

# This scripts calculates the mean population for each city and year.
# The script assumes your located in CSB/exercises/chapter3/3_8_1_measles_time_series/ when running it.

################################################
## Usage: python3 4_mean_pop_per_city_year.py ##
################################################

# import csv module to process csv data file
import csv

# store path to data and data file in string variable
datafile="../../../python/data/Dalziel2016_data.csv"

# create empty strings for city, year, population, and mean
city = ""
year = 0
pop = 0.0
mean = 0

# create empty dictionary for cities and years
city_year = {}


# open file
with open(datafile, 'r') as file1:
    count = 0
    # read file, with headers (first line) automatically stored as keys
    reader = csv.DictReader(file1)
    for row in reader:
        city = row["loc"]
        year = row["year"]
        pop = float(row["pop"])
        # if city not in cities dictionary, intitalize dictionary and subdictionary by using function .get 
        # (returns default value if key not present and intializes key)
        if city not in city_year:
            city_year[city] = city_year.get(city, {})
            city_year[city][year] = city_year[city].get(year, [pop, 1])
        # if year not in city's subdictionary, initialize subdictionary
        elif year not in city_year[city]: 
            city_year[city][year] = city_year[city].get(year, [pop, 1])
        else:
            city_year[city][year][0] += pop
            city_year[city][year][1] += 1


# calculate mean population per year, starting with one city
for city in city_year.keys():
    print(">", city, "<")
    print("YEAR | MEAN POP")
    print("-----|---------")
    for (year,pop) in city_year['CHICAGO'].items():
        mean = pop[0] / pop[1]
        print(year, "|", int(round(mean,0)))
    print("")