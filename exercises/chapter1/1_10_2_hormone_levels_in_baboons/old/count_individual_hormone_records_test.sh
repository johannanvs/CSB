#!/bin/bash

TEST
path=/mnt/c/Users/johanyst/ownCloud/Documents/bioinformatics_programming/practice/hp_qualified_courses/computing_for_biologists/CSB/unix/data
ids=$(tail -n +2 ${path}/Gesquiere2011_data.csv | cut -f 1 | sort -V | uniq)
# check if output stored correctly:
echo $ids # will print output without newlines
echo "$ids" # will print output with newlines (as output originally occurred)


# for each individual (i.e. unique entry), count the the number of times it was sampled
for id in $ids 
do 
	echo "Individual ID: " >> count_hormone_records_per_individual.txt
	echo "$id" >> count_hormone_records_per_individual.txt
	echo "Number of records: " >> count_hormone_records_per_individual.txt
	tail -n +2 ${path}/Gesquiere2011_data.csv | cut -f 1 | grep -c "$id" >> count_hormone_records_per_individual.txt
done

