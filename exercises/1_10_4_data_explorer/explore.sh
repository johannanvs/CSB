#!/bin/bash

# Last changes: 2020-10-07, Johanna von Seth

# Get stats for a column name of your choice in any csv file

# Launch script by writing: $ bash explore.sh path/to/input_file.csv column_number

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