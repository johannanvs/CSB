#!/bin/bash

# launch script by writing: $ bash netsize_all.sh path/to/input_files output_filename.txt

# store input path in variable
path=$1

# store filenames in variable
filenames=$(ls $1/)

#echo $filenames

# count and print the number of rows and columns for each file
for file in $filenames
do
	# count number of rows and store in variable:
	rows=$(wc -l < ${path}/"$file")
	# count the number of columns and store in variable
	columns=$(head -n1 ${path}/"$file" | awk '{print NF}')
	# Print collected information to standard out
	echo -n ${path}/"$file" >> $2
	echo -n " " >> $2
	echo -n "$rows" >> $2
	echo -n " " >> $2
	echo "$columns" >> $2	
done

# highest number of rows
echo -n "File with the highest number of rows: "
high_row=$(sort -t " " -nrk2 rows_columns.txt | head -n 1 | cut -d " " -f 1)
echo "$high_row"

# highest number of columns
echo -n "File with the highest number of columns: "
high_col=$(sort -t " " -nrk3 rows_columns.txt | head -n 1 | cut -d " " -f 1)
echo "$high_col"

# print output filename
echo ""
echo -n "In the output file "
echo -n $2
echo -n " you can find the number of rows and columns for all files in the directory "
echo $1/