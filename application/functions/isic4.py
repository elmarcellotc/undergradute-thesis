# This code is to assign a description to the products list
# You must run industries.py first

import pandas as pd
import os
import numpy as np
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

# uniques_products = []

# # open file and read the content in a list
# with open('dictionaries\products.txt', 'r') as fp:
#     for line in fp:
#         # remove linebreak from a current name
#         # linebreak is the last character of each line
#         x = line[:-1]

#         # add current item to the list
#         uniques_products.append(x)


# isic4 = isic4.loc[isic4['Code'].isin(uniques_products)]

print(isic4)

isic4.to_csv('dictionaries\isic4.csv', index=False)

papers = pd.read_csv('treatment_data\complete.csv')

from itertools import product

data = list(
    product(
    isic4['Code'].to_list(), papers['ID'].to_list()
    ))

pairs = pd.DataFrame(
    data, columns=['isic4_id', 'paper_id']
)

papers = papers[['ID', 'Text']]

pairs = pairs.merge(papers, how='left', left_on='paper_id', right_on='ID')
pairs = pairs.merge(isic4, how='left', left_on='isic4_id', right_on='Code')

pairs = pairs[['isic4_id', 'paper_id', 'Text', 'Description']]
pairs.rename(columns={'Text':'text1', 'Description':'text2'}, inplace=True)
pairs.dropna(inplace=True)
print(pairs)

pairs.to_csv('treatment_data\pairs.csv', index=False)