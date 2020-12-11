#!/bin/bash

# This scripts that one of the n*.txt files in CSB/unix/data/Saavedra2013/ and counts the number of rows and columns in the file.
# This script assumes your located in CSB/exercises/1_10_3_plant_pollinator_networks/.

##################################################################
## USAGE: bash 1_netsize.sh ../../unix/data/Saavedra2013/n1.txt ##
##################################################################

# count number of rows and store in variable:
rows=$(wc -l < "$1")

# count the number of columns and store in variable
columns=$(head -n1 "$1" | awk '{print NF}')

# Print collected information to standard out
echo -n "Filename: "
echo "$1"
echo -n "Number of rows: "
echo "$rows"
echo -n "Number of columns: "
echo "$columns"
