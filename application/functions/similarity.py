# This file create a similarity between the papers keywords and isic4 products
from datetime import datetime as dt

t1 = dt.now()
import os
os.chdir('..')

import pandas as pd
import numpy as np
import spacy
uni = pd.read_csv('treatment_data/complete.csv')
uni.dropna(inplace=True)

nlp = spacy.load('en_core_web_lg')

def get_similarity(doc1, doc2):
    doc1 = nlp(doc1)
    doc2 = nlp(doc2)
    
    return doc1.similarity(doc2)
        
# Load products

isic4 = pd.read_csv('dictionaries\isic4.csv')


# Then, select the uniques values to concat

uni1 = uni[['ID', 'Text']]

codes = isic4[['Code', 'Description']]
codes.columns = ['ID', 'Text']

similarity = np.ndarray(shape=(len(uni), len(isic4)))


for i in range(len(uni)):
    
    doc1 = uni['Text'].iloc[i]
    
    for j in range(len(isic4)):
        
        similarity[i][j] = get_similarity(doc1, isic4['Description'].iloc[j])
        
    print(f'paper: {uni.ID.iloc[i]} | min: {np.min(similarity[i])} | max: {np.max(similarity[i])} | mean: {np.mean(similarity[i])}')


similarity_df = pd.DataFrame(similarity)
similarity_df.columns = isic4['Code']
similarity_df['ID'] = uni['ID']
similarity_df = similarity_df[['ID']+isic4['Code'].to_list()]



similarity_df.to_csv('treatment_data/similarity.csv', index=False, encoding='utf-8')

print(similarity_df)

t2 = dt.now()-t1

with open('runtime/similarity_runtime.txt', 'w') as f:
    f.write('H:M:S '+str(t2))
f.close()


print('runtime (H:M:S): '+str(t2))