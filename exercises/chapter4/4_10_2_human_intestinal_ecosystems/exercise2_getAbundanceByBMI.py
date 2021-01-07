#!/usr/bin/env python

# Lahti et al. (2014) studied the microbial communities living in the intestines of 1000 individuals. They found that bacterial strains tend to be either absent or abundant, and posit that this would reflect bistability in these bacterial assemblages. The data used in this study are contained in the directory good_code/data/Lahti2014. The directory contains:
# Metadata.tab: characterizing each of the 1006 human records
# HITChip.tab: containing HITChip signal estimates of microbial abundance
# README: a description of the data by the study authors.

# 2. Write a function that takes as input the constraints (as above) and a bacterial “genus.” The function returns the average abundance (in logarithm base 10) of the genus for each BMI group in the subpopulation. For example, calling

#       get_abundance_by_BMI({"Time": "0", "Nationality": "US"}, "Clostridium difficile et rel.")

# should return

#       ______________________________________________
#       Abundance of Clostridium difficile et rel.
#       In subpopulation: 
#       ______________________________________________ 
#       Nationality -> US
#       Time -> 0 
#       ______________________________________________ 
#       3.08    NA
#       3.31    underweight
#       3.84    lean
#       2.89    overweight
#       3.31    obese
#       3.45    severeobese

target_genus = "Clostridium difficile et rel."

# import required modules
import csv

# define function
def get_abundance_by_BMI(constr_dict):
    # define Metadata dictionary
    metadata_dict = {}
    # define input file
    metadata_file = "Metadata.tab"
    # open metadata.tab file with dictreader
    with open(metadata_file) as infile1:
        # store headers as keys
        metadata = csv.DictReader(infile1, delimiter = '\t')
        # for each line, check that all constraints match
        for line in metadata:
            # use a Boolean to acertain that all constraints will be matched, and not just some of them
            all_matching = True
            # iterate over constraints dictionary
            for c in constr_dict:
            # if at least one doesn't match, skip line
                if line[c] != constr_dict[c]:
                    all_matching = False
                    break
            # if all match, store BMI_group as key and sample ID as value? Sample IDs will then be a list
            if all_matching == True:
                # store BMI group in variable
                line_bmi = line['BMI_group']
                # store sample ID in variable
                line_id = line['SampleID']
                # add BMI_group and sampleID
                if line_bmi in metadata_dict.keys():
                    metadata_dict[line_bmi] += [line_id]
                else:
                    metadata_dict[line_bmi] = [line_id]
    

    print(metadata_dict.values())
            
    # define HITChip dictionary
    hitchip_dict = {}
    # define input file 2
    hitchip_file = "HITChip.tab"
    # open HITChip.tab with dictreader
    with open(hitchip_file) as infile2:
        # store headers as key
        hitchipdata = csv.DictReader(infile2, delimiter = '\t')
        # for each line, if sample ID in metadata dictionary
        for line in hitchipdata:
            # store line sample ID in variable
            line_id = line['SampleID']
            for bmi, 
            # if sample ID from metadata dictionary match line sample ID
            if line_id in metadata_dict.values():
                # store bmi group of sample ID in hitchip dictionary
                print(metadata_dict[line_id])
        #    else:
        #        print(line_id, "not in metadata_dict")
        # store BMI_group from metadata dictionary of corresponding sample ID as key in HITChip dict and vinput     bacteria genus as dict value?   
        
        # 


# Call the function
get_abundance_by_BMI({"Time": "0", "Nationality": "US"})
