#!/bin/bash -l

# Last updated: 2021-01-19, Johanna von Seth

# Usage: bash exercise2_call_function.sh

# This scripts runs the python script exercise2_prob_rejected_year.py, located in the same directory, for all years entered in Fox2015_data.csv.

for year in 2004 2005 2006 2007 2008 2009 2010 2011 2012 2013 2014; do python3 exercise2_prob_rejected_year.py "$year"; done