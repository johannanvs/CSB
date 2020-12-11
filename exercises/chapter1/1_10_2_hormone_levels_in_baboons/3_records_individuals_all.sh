#!/bin/bash

# Date: 2020-12-11, Johanna von Seth

# This scripts counts the number of times the blood level of all individuals were recorded. 
# The scripts assumes your located in CSB/exercises/chapter1/1_10_2_hormone_levels_in_baboons/.

##############################################
## Usage: bash 3_records_individuals_all.sh ##
##############################################

# Store the output filename in a variable
outfile="record_count_per_individual.txt"

# Store the relative path to the data directory
datadir=../../../unix/data

# Store the data filename in a variable
data="Gesquiere2011_data.csv"

# Store the relative path to the location of the script (this is where the output file should be)
outdir=../../exercises/chapter1/1_10_2_hormone_levels_in_baboons


# Change to the folder where the data file is located
cd ${datadir}/

# Extract all unique individual ID's
ids=$(tail -n +2 Gesquiere2011_data.csv | cut -f 1 | sort -V | uniq)

# For each individual, count the number of times the blood level was recorded
for id in $ids 
do 
	echo -e "\nIndividual ID: " >> "$outfile"
	echo "$id" >> "$outfile"
	echo "Number of records: " >> "$outfile"
	cut -f 1 "$data" | grep -wc "$id" >> "$outfile"
done

mv "$outfile" ${outdir}/"$outfile"

echo -e "\nDone! The output can be found in the script directory, with the filename $outfile.\n"