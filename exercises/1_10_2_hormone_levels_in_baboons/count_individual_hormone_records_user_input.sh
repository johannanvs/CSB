#!/bin/bash

# launch script by writing: $ bash count_individual_hormone_records_user_input.sh path/to/input_file.csv individual_ID

# based on the format of Gesquiere2011_data.csv, which actually *not* a csv file

# take a tab delimited ($1 = first argument)
# remove the header
tail -n +2 $1 > $1.tmp1
# extract columns
cut -f 1 $1.tmp1 > $1.tmp2
# find all entries of input individual ($2 = second argument) and count number of entries
grep -c $2 $1.tmp2 
# remove temporary, intermediate files
rm $1.tmp*