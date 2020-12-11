#!/usr/bin/env python
# coding: utf-8

# Date: 2020-12-11, Johanna von Seth


# import necessary modules
import sys
import statistics

# create and define function to compute mean r of input taxon
def compute_mean_r(input_file="../../../good_code/data/Jiang2013_data.csv", 
                  input_taxon="Fish"):
    """
    Take a desired Taxon from 'CSB/good_code/data/Jiang2013_data.csv' as input and return it's mean value of r (mating).
    A positive mean r stands for assortative mating, and a negative to disassortative mating.

    Usage: python3 1_mean_mating.py path/to/input_file input_taxon

    =================================
    Unit testing with docstrings
    =================================
    Run the command in python3, (e.g.python3 -i 1_mean_mating.py ../../../good_code/data/Jiang2013_data.csv Fish) 
    and copy the output below:
    
    >>> compute_mean_r("../../../good_code/data/Jiang2013_data.csv", "Fish")
    The mating mean of taxon Fish is: 0.397
    Since the mean value of r is positive, this taxon mostly consist of species with assortative mating.

    >>> compute_mean_r("../../../good_code/data/Jiang2013_data.csv", "Amphibian")
    The mating mean of taxon Amphibian is: 0.186
    Since the mean value of r is positive, this taxon mostly consist of species with assortative mating.

    >>> compute_mean_r("../../../good_code/data/Jiang2013_data.csv", "Bird")
    The mating mean of taxon Bird is: 0.132
    Since the mean value of r is positive, this taxon mostly consist of species with assortative mating.

    """
    
    ## extracting data from input file ##

    # define list for r values
    mating = []

    # open file
    with open(input_file) as infile:
        # process line by line
        for line in infile:
            # skip blank lines
            if line.strip():
                # split line into columns
                column = line.strip().split("\t")
                # store line taxon in a variable, make lowercase
                line_taxon = column[1].lower()
                # store line r in a variable
                line_mating = column[3]
                # if lowercase input taxon = lowecase line taxon
                if input_taxon.lower() == line_taxon:
                    # add line r value to the list
                    mating.append(float(line_mating))

    ## calculate mean value of r for input taxon ##

    mean_r = statistics.mean(mating)
    print("The mating mean of taxon", input_taxon, "is:", round(mean_r, 3))
    if mean_r < 0:
        print("Since the mean value of r is negative, this taxon mostly consist of species with disassortative mating.")
    else:
        print("Since the mean value of r is positive, this taxon mostly consist of species with assortative mating.")



if __name__ == "__main__":
    import doctest
    doctest.testmod()
    # read the arguments on the command line 
    # (they are strings by default)
    user_file = sys.argv[1]
    user_taxon = sys.argv[2]
    # call the function
    compute_mean_r(user_file, user_taxon)

