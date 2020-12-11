#!/bin/bash

# Date 2020-12-11, Johanna von Seth

# This scripts outputs the filenames of the files with the largest number of rows and columns, respectively, in directory CSB/unix/data/Saavedra2013/.
# This script assumes your located in CSB/exercises/chapter1/1_10_3_plant_pollinator_networks/, and that you have run 2_netsize_all.sh prior to running this script.

#####################################
## Usage: bash 3_largest_number.sh ##
#####################################

# store input file in variable
summaryfile="summary.txt"

# path to n*.txt files:
path=../../../unix/data/Saavedra2013

# find highest number of rows
echo -ne "\nFile with the highest number of rows: "
high_row=$(sort -k 2nr $summaryfile | head -n 1 | cut -d " " -f 1)
echo "$high_row"

# find highest number of columns
echo -n "File with the highest number of columns: "
high_col=$(sort -k 3nr $summaryfile | head -n 1 | cut -d " " -f 1)
echo "$high_col"

# print output filename
echo ""
echo -n "In the file "
echo -n $summaryfile
echo -n " (located in the same directory as this script) you can find the number of rows and columns for all files in the directory "
echo ${path}/
echo ""