# This code is to assign a description to the products list
# You must run industries.py first

import pandas as pd
import os
os.chdir('..')

# Read descriptions file
isic4 = pd.read_csv('dictionaries/isic4_base.csv')

# Assign correct code:

isic4_codes = isic4['Code'].to_list()

for i in range(len(isic4_codes)):
    
    # Complete code
    if isic4_codes[i].isnumeric():
        while len(isic4_codes[i]) < 4:
            isic4_codes[i] = '0'+isic4_codes[i]
            
        isic4_codes[i] = k + isic4_codes[i]
            
    else:
        k = isic4_codes[i]
           
isic4['Code'] = isic4_codes
            
isic4 = isic4.loc[isic4['Code'].str.len() > 1]

uniques_products = []

# open file and read the content in a list
with open('dictionaries\products.txt', 'r') as fp:
    for line in fp:
        # remove linebreak from a current name
        # linebreak is the last character of each line
        x = line[:-1]

        # add current item to the list
        uniques_products.append(x)


isic4 = isic4.loc[isic4['Code'].isin(uniques_products)]

print(isic4)

isic4.to_csv('dictionaries\isic4.csv', index=False)