#!/bin/bash

# Last changes: 2020-12-11, Johanna von Seth

# This script can be used to get stats for a column name of your choice in any csv file
# The scripts assumes your located in CSB/exercises/1_10_4_data_explorer/.

#################################################################
## Usage: bash explore.sh path/to/input_file.csv column_number ##
#################################################################

file=$1
col=$2

echo "Column name:"
# print column name
head -n 1 "$file" | cut -d "," -f "$col"

echo "Number of distinct values:"
# print number of distinct values in column
tail -n +2 "$file" | cut -d "," -f "$col" | sort -V | uniq | wc -l

echo "Minimum values:"
# print minimum value in column
tail -n +2 "$file" | cut -d "," -f "$col" | sort -V | uniq | head -n 1

echo "Maximum value:"
# print maximum value in column
tail -n +2 "$file" | cut -d "," -f "$col" | sort -rV | uniq | head -n 1