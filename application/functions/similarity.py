# This file create a similarity between the papers keywords and isic4 products
from datetime import datetime as dt

t1 = dt.now()
import os
os.chdir('..')

import pandas as pd
import numpy as np
import spacy

nlp = spacy.load('en_core_web_lg')

def get_similarity(doc1, doc2):
    doc1 = nlp(doc1)
    doc2 = nlp(doc2)
    
    return doc1.similarity(doc2)
        
# Load products

pairs = pd.read_csv('treatment_data\pairs.csv')

# Then, select the uniques values to concat

pairs['similarity'] = pairs.apply(lambda x: get_similarity(x['text1'], x['text2']), axis = 1)


pairs = pairs[['isic4_id', 'paper_id', 'similarity']]

pairs.to_csv('treatment_data/similarity.csv', index=False, encoding='utf-8')

print(pairs)

t2 = dt.now()-t1

with open('runtime/similarity_runtime.txt', 'w') as f:
    f.write('H:M:S '+str(t2))
f.close()


print('runtime (H:M:S): '+str(t2))