#!/usr/bin/env python

"""
Last updated: 2021-01-19, Johanna von Seth

Note! To run this script for all years, simply enter on the command line:
bash exercise2_call_function.sh

Usage: python3 exercise2_prob_rejected_year.py year

This script contains a function that counts the number of reviewers per manuscript and measures the probability of rejection per user defined year. The script assumes you're located in CSB/exercises/chapter6/6_6_2_number_of_reviewers_and_rejection_rate.

"""

# import modules
import sys
import pandas
import numpy as np

# read file with pandas
foxdata = pandas.read_csv("../../../scientific/data/Fox2015_data.csv")

def rejection_probability(input_year):
    # get the unique MsID's by storing 'MsID' as a list and then a set 
    unique_ms = list(set(foxdata['MsID']))
    
    # store number of reviewers, final decision, and year in individual lists
    revs = []
    decision = []
    year = []
    
    # loop over unique_ms, one msID at a time
    for ms in unique_ms:
        # extract corresponding rows for data file
        subset = foxdata[foxdata["MsID"] == ms]
        # summarize number of reviewers and add to list
        revs.append(sum(subset["ReviewerAgreed"]))
        # extract final decision 
        # for all entries of one msID, the finaldecision will be the same
        # thus, checking only the first position is enough
        if list(subset["FinalDecision"])[0] == 1:
            decision.append(1)
        else:
            decision.append(0)
        # extract year
        year.append(str(list(subset["Year"])[0]))

    # convert lists into arrays using numpy
    # List of number of reviewers per manuscript
    revs = np.array(revs)
    # List of final decision per manuscript
    decision = np.array(decision)
    # List of year per manuscript
    year = np.array(year)

    if input_year != "all":
        # extract data from user defined year
        # extract number of reviewers at the same index positons as input_year are in list year
        revs = revs[np.where(year == input_year)]
        decision = decision[np.where(year == input_year)]

    # store no of submissions and overall rejection rate of the year
    submissions = len(decision)
    overall_reject_rate = round(decision.mean(), 3)

    # print output
    print("===============================")
    print("Year:", input_year)
    print("Submissions:", submissions)
    print("Overall rejection rate:", overall_reject_rate)
    print("NumRev", "\t", "NumMs", "\t", "rejection rate")
    # loop over the number of reviewers for the input year
    for i in range(max(revs) + 1):
        print(i, "\t",
            # print number of manuscripts by taking the length of decisions list
            len(decision[revs == i]), "\t",
            # print rejection rate by taking the mean of decisions for each no. of reviewers
            round(decision[revs == i].mean(), 3))
    print("===============================")


if __name__ == "__main__":
  # read the arguments on the command line 
  # (they are strings by default)
  user_year = sys.argv[1]
  # call the function
  rejection_probability(user_year)
