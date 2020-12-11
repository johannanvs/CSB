#!/bin/bash

# Date: 201210, Johanna von Seth

# This scripts counts the number of times the blood level of individuals 3 and 27 were recorded. 
# The scripts assumes your located in CSB/exercises/1_10_2_hormone_levels_in_baboons/.

# Change to the folder where the data file is located
cd ../../unix/data/

# Filter out all record entries with individual 3
echo -e "\nNumber of record entries for individual 3:"
cut -f 1 Gesquiere2011_data.csv | grep -cw 3

# Filter out all record entries with individual 27
echo -e "\nNumber of record entries for individual 27:"
cut -f 1 Gesquiere2011_data.csv | grep -cw 27
echo ""
