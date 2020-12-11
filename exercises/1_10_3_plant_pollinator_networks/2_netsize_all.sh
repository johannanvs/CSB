#!/bin/bash

# Date 2020-12-11, Johanna von Seth

# This scripts takes all the n*.txt files in CSB/unix/data/Saavedra2013/ and counts the number of rows and columns in for each file.
# This script assumes your located in CSB/exercises/1_10_3_plant_pollinator_networks/.

####################################################################################
## Usage: bash 2_netsize_all.sh ../../unix/data/Saavedra2013 output_filename.txt ##
####################################################################################

# store input path in variable
path=$1

# store output filename in variable
outfile=$2

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

# highest number of rows
echo -ne "\nFile with the highest number of rows: "
high_row=$(sort -k 2nr $outfile | head -n 1 | cut -d " " -f 1)
echo "$high_row"

# highest number of columns
echo -n "File with the highest number of columns: "
high_col=$(sort -k 3nr $outfile | head -n 1 | cut -d " " -f 1)
echo "$high_col"

# print output filename
echo ""
echo -n "In the output file "
echo -n $outfile
echo -n " (located in the same directory as this script) you can find the number of rows and columns for all files in the directory "
echo ${path}/
echo ""