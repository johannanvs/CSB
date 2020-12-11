#!/bin/bash

# launch script by writing: $ bash count_individual_hormone_records.sh path/to/input_file.csv output_filename

# based on the format of Gesquiere2011_data.csv, which actually *not* a csv file

# take a tab delimited ($1 = first argument)
# remove the header, extract column with IDs, sort them, keep only unique entries, store everything in a variable
ids=$(tail -n +2 $1 | cut -f 1 | sort -V | uniq) 

# for each individual (i.e. unique entry), count the the number of times it was sampled and store in output file ($2 = second argument)
for id in $ids 
do 
	echo "Individual ID: " >> $2
	echo "$id" >> $2
	echo "Number of records: " >> $2
	tail -n +2 $1 | cut -f 1 | grep -c "$id" >> $2
done

