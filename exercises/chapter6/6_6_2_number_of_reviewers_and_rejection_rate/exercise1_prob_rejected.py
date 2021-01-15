#!/usr/bin/env python

"""
Last updated: 2021-01-14, Johanna von Seth

Usage: python3 exercise1_prob_rejected.py

This script counts the number of reviewers per manuscript and measures the probability of rejection. The script assumes you're located in CSB/exercises/chapter6/6_6_2_number_of_reviewers_and_rejection_rate.

"""

# import modules
import pandas
import numpy as np

# read file with pandas
foxdata = pandas.read_csv("../../../scientific/data/Fox2015_data.csv")

# check names of columns
#print(foxdata.columns)
# out: Index(['MsID', 'Year', 'HandlingEditorSex', 'ReviewerSex', 'ReviewerRegion',
#       'ReviewerInvited', 'ReviewerAgreed', 'ReviewerScore', 'FinalDecision'],
#      dtype='object')


# get the unique MsID's by storing 'MsID' as a list and then a set 
uniq_ms = list(set(foxdata['MsID']))
#num_ms = len(uniq_ms)
#print(num_ms)

# store number of reviewers, final decision, and year in individual lists
num_rev = []
decision = []
year = []

# extract corresponding info from data file, by using the list of unique MsID's
for ms in uniq_ms:
	# extract corresponding rows
	subset = foxdata[foxdata.MsID == ms]
	# summarize number of reviewers and add to list
	num_rev.append(sum(subset["ReviewerAgreed"]))
	# extract final decision 
	# for all entries of one msID, the finaldecision will be the same
	# thus, checking only the first position is enough
	if list(subset["FinalDecision"])[0] == 1: 
		decision.append(1)
	else:
		decision.append(0)
	# extract year
	year.append(list(subset["Year"])[0])

# convert lists into arrays using numpy
num_rev = np.array(num_rev)
decision = np.array(decision)
year = np.array(year)

# measure and print rejection rate for each number of reviewers
# number of submissions
num_submit = len(decision)
reject_rate = round(decision.mean(), 3)

print("=============================")
print("Submissions:", num_submit)
print("Overall rejection rate:", reject_rate)
print("NumRev", "\t", 
	"NumMS", "\t",
	"RejectRate")
# get the rejection rate per number of reviewers
for i in range(max(num_rev) + 1):
	print(i, "\t",
		len(decision[num_rev == i]), "\t",
		round(decision[num_rev == i].mean(), 3))
print("=============================")















