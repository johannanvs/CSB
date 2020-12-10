#!/bin/bash

# Date: 201210, Johanna von Seth

# This script is used to process the file "Marra2014_data.fasta" to answer some simple questions. It assumes you run the script from the CSB/exercises/1_10_1_next_generation_sequencing_data/ folder, and that the filesystem within CSB is the same


# 1. Change directory to CSB/unix/sandbox.
cd ../../unix/data/

# 2. What is the size of the file Marra2014_data.fasta?
echo -e "\nThe file size of Marra2014_data.fasta is:"
ls -lh | grep Marra2014_data.fasta | awk '{print $5}'

# 3. Create a copy of Marra2014_data.fasta in the sandbox and name it my_file.fasta.
cp Marra2014_data.fasta my_file.fasta

# 4. How many contigs are classified as isogroup00036?
echo -e "\nNumber of contigs classified as isogroup00036:"
grep -c 'gene=isogroup00036' my_file.fasta

# 5. Replace the original “two-spaces” delimiter with a comma.
cat my_file.fasta | sed 's/  /,/g' > my_file_fasta.csv
echo -e "\nThis is what the headers look like if the spaces are replaced with a comma:"
grep '^>' my_file_fasta.csv | head

# 6. How many unique isogroups are in the file?
echo -e "\nNumber of unique isogroups in file:"
grep '^>' my_file.fasta | awk '{print $4}' | sort | uniq | wc -l

# 7. Which contig has the highest number of reads (numreads)? How many reads does it have?
echo -e "\nName of contig with the highest number of reads:"
grep '^>' my_file.fasta | awk '{print $1,$3}' | sed 's/numreads=//g' | sort -k 2nr | head -n 1 | sed 's/>//g' | awk '{print $1}'
echo -e "\nNumber of reads:"
grep '^>' my_file.fasta | awk '{print $1,$3}' | sed 's/numreads=//g' | sort -k 2nr | head -n 1 | sed 's/>//g' | awk '{print $2}'
echo ""

# Remove files that were generated with this script
rm my_file.fasta
rm my_file_fasta.csv