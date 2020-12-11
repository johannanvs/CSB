#!/bin/bash

# Date: 2020-12-11, Johanna von Seth

# This script counts the number of records of one individual, based on user input.
# The scripts assumes your located in CSB/exercises/chapter1/1_10_2_hormone_levels_in_baboons/.

#############################################################################################################
## Usage: bash 2_records_individuals_user_input.sh ../../../unix/data/Gesquiere2011_data.csv individual_id ##
#############################################################################################################

# first input = inputfile = $1
# second input = individual_id = $2

echo -e "\nNumber of record entries for individual $2:"
cut -f 1 $1 | grep -cw $2
echo "" 