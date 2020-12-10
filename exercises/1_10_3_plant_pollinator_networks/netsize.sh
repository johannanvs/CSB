#!/bin/bash

# launch script by writing: $ bash netsize.sh path/to/input_file.txt

# count number of rows and store in variable:
rows=$(wc -l < "$1")

# count the number of columns and store in variable
columns=$(head -n1 "$1" | awk '{print NF}')

# Print collected information to standard out
echo -n "Filename: "
echo "$1"
echo -n "Number of rows: "
echo "$rows"
echo -n "Number of columns: "
echo "$columns"
