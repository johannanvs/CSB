#!/usr/bin/env python
# coding: utf-8

# In[2]:


# In their article, Dalziel et al. (2016) provide a long time series reporting the
# numbers of cases of measles beforemass vaccination, for many US cities. The
# data consist of cases in a given US city for a given year, and a given biweek
# of the year (i.e., first two weeks, second two weeks, etc.). The time series is
# contained in the file Dalziel2016_data.csv.


# In[12]:


# 1. Write a program that extracts the names of all the cities in the database (one entry per city).

# import modules
import csv

# create empty list
cities = []

# open file
with open("../data/Dalziel2016_data.csv") as infile:
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


# In[31]:


# 2. Write a program that creates a dictionary where the keys are the cities 
# and the values are the number of records (rows) for that city in the data.

# import modules
import csv

# create an empty list
cities_list = []

# create an empty dictionary
cities_dict = {}

# open file
with open("../data/Dalziel2016_data.csv") as infile:
    count = 0
    # read file and convert each row to a dictionary, where the headers in the first line are automatically saved as the keys
    reader = csv.DictReader(infile)
    for row in reader:
        count += 1
        # if the city is not in the list, add it to the list and add the city as key to a dictionary (with value = 1 since it's the first row)
        if row["loc"] not in cities_list:
            cities_list.append(row["loc"])
            cities_dict[row["loc"]] = 1
        else:
            # increase the city's value with one, since another row has been found
            cities_dict[row["loc"]] += 1
        #if count > 50:
            #break

print(len(cities_list))
print(count)
print(count/len(cities_list))
cities_dict.items()


# In[63]:


# 3. Write a program that calculates the mean population for each city,
# obtained by averaging the values of pop.

import csv

# create an empty dictionary
cities = {}

# open data file
with open("../data/Dalziel2016_data.csv") as infile:
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


# In[146]:


# 4. Write a program that calculates the mean population for each city and year.

# Need to do a similar thing as for 3., but the value for each city in the directory should be another directory, 
# with year as key and population + number of lines in list as value

# import modules
import csv

# create empty strings for city, year, and population
city = ""
year = 0
pop = 0.0

# create empty dictionary for cities and years
city_year = {}


# open file
with open("../data/Dalziel2016_data.csv", 'r') as file1:
    count = 0
    # read file, with headers (first line) automatically stored as keys
    reader = csv.DictReader(file1)
    for row in reader:
        #count += 1
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
        #if count > 200:
            #break

mean = 0

# calculate mean population per year, starting with one city
for city in city_year.keys():
    print(">", city, "<")
    print("YEAR | MEAN POP")
    print("-----|---------")
    for (year,pop) in city_year['CHICAGO'].items():
        mean = pop[0] / pop[1]
        print(year, "|", int(mean))
    print("")


# In[ ]:




