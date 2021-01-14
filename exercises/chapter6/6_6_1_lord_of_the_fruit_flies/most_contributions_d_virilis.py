#!/usr/bin/env python

"""
Last updated: 2021-01-14, Johanna von Seth

Usage: python3 most_contributions_d_virilis.py

This script identifies the five authors that published most contributions on D. virilis. The script assumes you're located in CSB/exercises/chapter6/6_6_1_lord_of_the_fruit_flies.

"""

# import modules
from Bio import Entrez
import re

# 1. Identify the number of papers in the PubMed database that have the words 
# Drosophila virilis in their title or abstract.

# query the PubMed database and extract papers that contain Drosophila virilis in their title/abstract
Entrez.email = "johanna.vonseth@nrm.se"
handle = Entrez.esearch(db = "pubmed",
                       term = ("Drosophila virilis[Title/Abstract]"),
                       usehistory = "y")

# parse results and convert to Python dictionary
record = Entrez.read(handle)
handle.close()

# how many hits?
record["Count"]
# Out: 554

# store WebEnv and QueryKey in variables for later
webenv = record["WebEnv"]
query_key = record["QueryKey"]

# 2. Retrieve the PubMed entries that were identified in step (1).
# retrieve data
Entrez.email = "johanna.vonseth@nrm.se"
handle = Entrez.efetch(db = "pubmed",
                      rettype = "medline",
                      retmode = "text",
                      webenv = webenv,
                      query_key = query_key)
out_handle = open("d_virilis_abstracts.txt", "w")
hits = handle.read()
handle.close()
out_handle.write(hits)
out_handle.close()





