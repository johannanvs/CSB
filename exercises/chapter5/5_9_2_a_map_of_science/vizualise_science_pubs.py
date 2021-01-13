#!/usr/bin/env python

"""
Last updated: 2021-01-13, Johanna von Seth

Usage: python3 exercise1_extract_zip_code.py

This script creates a plot showing the geographical locations of the authors that published in Science during 2015. The script assumes you're located in CSB/exercises/chapter5/5_9_2_a_map_of_science.

"""

# import modules
import re
import csv
import matplotlib.pyplot as plt

# store path to files in variables
pubmedfile = "../../../regex/data/MapOfScience/pubmed_results.txt"
zipcoordfile = "../../../regex/data/MapOfScience/zipcodes_coordinates.txt"

# open pubmed_results.txt file
with open(pubmedfile) as f:
	# read to whole file at once
	my_text = f.read()
	# use regex replace new line and the following 6 spaces with a single space, so that every entry is on a single line
	my_text = re.sub(r'\n\s{6}',' ', my_text)

# compile a regex that captures all US zip codes
zipcodes = re.findall(r'[A-Z]{2}\s(\d{5}), USA', my_text)

# extract unique zipcodes by converting the list to a set, and then a list again
unique_zipcodes = list(set(zipcodes))
# zipcodes_coordinates.txt is sorted, so this list should be too.
unique_zipcodes.sort()

# create required lists
zip_code = []
zip_long = []
zip_lat = []
zip_count = []

# open zipcodes_coordinates.txt file with dictreader
with open(zipcoordfile) as f:
	coorddata = csv.DictReader(f, delimiter = ',')
	# for each line
	for line in coorddata:
		# if zipcode is in unique_zipcodes list
		if line['ZIP'] in unique_zipcodes:
			#z = line['ZIP']
			# add zipcode to zip_code, longitute to zip_long, latitude to zip_lat, and the number of occurrences of zipcode in pubmed_results.txt
			zip_code.append(line['ZIP'])
			zip_long.append(float(line['LNG']))
			zip_lat.append(float(line['LAT']))
			zip_count.append(zipcodes.count(line['ZIP']))

# Plot the results
#%matplotlib inline # SyntaxError here if unhashed, because the code is not run in iPython
plt.scatter(zip_long, zip_lat, s = zip_count, c= zip_count)
plt.colorbar()
# only continental us without Alaska
plt.xlim(-125,-65)
plt.ylim(23, 50)
# add a few cities for reference (optional)
ard = dict(arrowstyle="->")
plt.annotate('Los Angeles', xy = (-118.25, 34.05),
				xytext = (-108.25, 34.05), arrowprops = ard)
plt.annotate('Palo Alto', xy = (-122.1381, 37.4292),
				xytext = (-112.1381, 37.4292), arrowprops= ard)
plt.annotate('Cambridge', xy = (-71.1106, 42.3736),
				xytext = (-73.1106, 48.3736), arrowprops= ard)
plt.annotate('Chicago', xy = (-87.6847, 41.8369),
				xytext = (-87.6847, 46.8369), arrowprops= ard)
plt.annotate('Seattle', xy = (-122.33, 47.61),
				xytext = (-116.33, 47.61), arrowprops= ard)
plt.annotate('Miami', xy = (-80.21, 25.7753),
				xytext = (-80.21, 30.7753), arrowprops= ard)
params = plt.gcf()
plSize = params.get_size_inches()
params.set_size_inches( (plSize[0] * 3, plSize[1] * 3) )
plt.show()

