# We use a dictionary to store the results
BMI_IDs = {}
# Open the file, build a csv DictReader
with open('../data/Lahti2014/Metadata.tab') as f:
    csvr = csv.DictReader(f, delimiter = '\t')
    for row in csvr:
        # check that all conditions are met
        matching = True
        for e in dict_constraints:
            if row[e] != dict_constraints[e]:
                # The constraint is not met. Move to the next record
                matching = False
                break
        # matching is True only if all the constraints have been met
        if matching == True:
            # extract the BMI_group
            my_BMI = row['BMI_group']
            if my_BMI in BMI_IDs.keys():
                # If we've seen it before, add the SampleID
                BMI_IDs[my_BMI] = BMI_IDs[my_BMI] + [row['SampleID']]
            else:
                # If not, initialize
                BMI_IDs[my_BMI] = [row['SampleID']]