#!/bin/bash

# Date 2020-12-11, Johanna von Seth

# This scripts takes all the n*.txt files in CSB/unix/data/Saavedra2013/ and counts the number of rows and columns in for each file.
# This script assumes your located in CSB/exercises/1_10_3_plant_pollinator_networks/.

###############################################################
## Usage: bash 2_netsize_all.sh ../../unix/data/Saavedra2013 ##
###############################################################

# store input path in variable
path=$1

# store output filename in variable
outfile="summary.txt"

# store filenames in variable
filenames=$(ls $path/)

# Add header to output file (optional)
#echo -n "filename" >> $outfile
#echo -n " " >> $outfile
#echo -n "rows" >> $outfile
#echo -n " " >> $outfile
#echo -n "columns" >> $outfile
#echo "" >> $outfile

# count and print the number of rows and columns for each file
for file in $filenames
do
	# count number of rows and store in variable:
	rows=$(wc -l < ${path}/"$file")
	# count the number of columns and store in variable
	columns=$(head -n1 ${path}/"$file" | awk '{print NF}')
	# Print collected information to output file
	echo -n "$file" >> $outfile
	echo -n " " >> $outfile
	echo -n "$rows" >> $outfile
	echo -n " " >> $outfile
	echo "$columns" >> $outfile	
done


# print output filename
echo ""
echo -n "Done! In the output file "
echo -n $outfile
echo -n " (located in the same directory as this script) you can find the number of rows and columns for all files in the directory "
echo ${path}/
echo ""