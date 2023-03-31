# Go to general directory

from table_export import export_to_latex, export_to_word
import os
os.chdir('..')

# Workeable libraries

import pandas as pd
import numpy as np
from matplotlib import pyplot as plt


# ## <center>**PAPERS CLASSIFICATION METHODOLOGY**</center>
# 
# Given the similarity between the papers text, and the isic4 codes descriptions, I generated a similarity matrix between the papers and the product code using the SpaCy library. This notebook is made to define a cutoff to classify with 1 or 0 the each paper.
# 
# 
# ### **THE SIMILARITY MATRIX**
# 
#  The similarity matrix contains the isic4 product code in per column, and the paper code per row index. The current matrix contains 415 columns, and 8195 rows


similarity = pd.read_csv('treatment_data/similarity.csv', index_col=0)
    
export_to_latex(similarity.reset_index().iloc[[0,25,62,80,100], [0,25,62,80,100]], 'similarity_example.tex')
export_to_word(similarity.reset_index().iloc[[0,25,62,80,100], [0,25,62,80,100]], 'similarity_example.docx')

similarity.reset_index().iloc[[0, 25, 62, 80, 100], [0, 25, 62, 80, 100]]


# This code shows the cutoff by all the 
range_base = np.arange(0, 1.01, 0.01)

# Count of observations bigger or equal to the cutoff
count_array = np.zeros(range_base.shape[0])

similarity_matrix = similarity.iloc[:,1:].to_numpy()
for i in range(range_base.shape[0]):
    count_array[i] = (np.where(similarity_matrix>=range_base[i], 1, 0)).sum()
    
# Get the possible values. Also, get free space after redefine similarity_matrix

plt.plot(
    range_base, (count_array / (similarity_matrix.shape[0] * similarity_matrix.shape[1])),
    linewidth=6
)
plt.rcParams['font.size'] = 18
plt.savefig('outputs/graphs/g1_portion_classified.jpg', dpi=600)


range_base = np.arange(0, 1.01, 0.01)

# We first generate the letter codes

codes_columns = similarity.columns[1:].to_list()

products_codes = [x[0] for x in codes_columns]

products_codes = np.unique(products_codes)

###################################################
### This commented code is to plot by ISIC4 type
##########################################

#######################################################################
for j in products_codes:

    columns_list = [i for i in codes_columns if j in i]
    col_array = similarity[columns_list].to_numpy()

    count_array = np.zeros(range_base.shape[0])

    for i in range(range_base.shape[0]):
        count_array[i] = (np.where(col_array>=range_base[i], 1, 0)).sum()

    col_array = col_array.shape[0] * col_array.shape[1]

    plt.plot(range_base, (count_array / col_array), linewidth=4)
####################################################################
plt.rcParams['font.size'] = 18
plt.savefig('outputs/graphs/g1_2_portion_classified_per_code.jpg', dpi=600)



# The graph 1.2 shows that there is an important difference in the portion of papers classified per cutoff. This make relevant to have a different cutoff depending on the code letter


# This code is to show the distribution of the similarity values:

plt.hist(similarity_matrix.flatten(), bins = np.arange(0, 1.001, 0.001), density=True)
plt.axvline(similarity_matrix.flatten().mean(), color='k', linestyle='dashed', linewidth=4)
plt.axvline(similarity_matrix.flatten().mean()+similarity_matrix.flatten().std(), color='k', linestyle='dashed', linewidth=3)
plt.axvline(similarity_matrix.flatten().mean()-similarity_matrix.flatten().std(), color='k', linestyle='dashed', linewidth=3)
plt.rcParams['font.size'] = 18
plt.savefig('outputs/graphs/g1_3_similarity_frequency.jpg')


# ### THE GENERAL CUTOFF
# 
# Seen the data showed, to select a general cutoff of 0.8 shows as a good initial point to classify the papers. The next code shows the products for what each papers is classified:


papers_list = [None]*len(similarity)

code_list = similarity.columns.to_numpy()

classification_list = list(
    map(
        lambda X, Y: ('-').join(
            [x for y in Y for x in X if y >= 0.75]
        ), [code_list]*len(similarity), similarity_matrix
    )
)
    
papers = pd.DataFrame({'ID':similarity.index.to_list(), 'product':classification_list})


# Now, we import the information of the papers to append then to the hole data frame


complete = pd.read_csv('treatment_data/complete.csv')

preview_list = [i for i in range(5)]

show_rows, show_cols = [np.random.randint(0,8000) for i in range(50)],[np.random.randint(0,400) for i in range(50)]
    
export_to_latex(complete.iloc[preview_list, preview_list], 'papers_data.tex')
export_to_word(complete.iloc[preview_list, preview_list], 'papers_data.docx')



complete = complete.iloc[show_rows, :]


# Now, I add the province of the paper, and the province of the paper, and the city

papers1 = papers
# Be sure taht you have the IDs columns as str
complete['ID'] = complete['ID'].astype(str)
papers1['ID'] = papers1['ID'].astype(str)

# merge on the left
papers1 = complete.merge(papers1, how='left', on='ID')

# Save as latex to the paper


# The next step takes a between one or two hours. The idea is to first, get the data of the other papers that are not the same, but contains st least one common author.


papers2 = papers1.copy()

papers2.pop('Text')

papers2_matrix = papers2.to_numpy()


publication_matrix = np.array([np.concatenate((x, y)) for x in papers2_matrix for y in papers2_matrix])



# Now, we need to know how connected are the publications with the others. That can be made with the authors and references columns
# The idea is to set a connection as a paper that contains the authors from another in their references

# The output dataframe must have the following columns

# - id: name identifier of the publication
# - year: year of the publication
# - province: 
# - city
# - product: list of products isic4. In the next cells, it will be multiple observations thank of multiple isic4 products per paper

publications = pd.DataFrame(publication_matrix)
publications.columns = ['iid', 'iyear', 'iprovince', 'icity', 'iauthor', 'iproduct', 'oid', 'oyear', 'oprovince', 'ocity', 'oauthor', 'oproduct']
publications = publications.loc[publications['iid']!=publications['oid']]

# First explode by author. This will make easier to select the papers with the same authors

publications['iauthor'] = publications['iauthor'].str.split(', ')
publications['oauthor'] = publications['oauthor'].str.split(', ')
publications = publications.explode(['iauthor'])
publications = publications.explode(['oauthor'])

publications = publications.loc[publications['iauthor']==publications['oauthor']]

# Now, we explode by products, and remove those observations without products

publications['iproduct'] = publications['iproduct'].str.split('-')
publications['oproduct'] = publications['oproduct'].str.split('-')
publications = publications.explode(['iproduct'])
publications = publications.explode(['oproduct'])
publications = publications.loc[publications['iproduct']!='']
publications = publications.loc[publications['oproduct']!='']

# It must be the first paper. Probably publication have repeated observations but flipping i with o

publications = publications.loc[publications['iyear']<publications['oyear']]

# Pop non required columns:

publications.pop('iauthor')
publications.pop('oauthor')

publications.to_csv('treatment_data/publications.csv')
publications = publications.iloc[[np.random.randint(0,len(publications)) for i in range(5)],:]

export_to_latex(publications, 'publications.tex')
export_to_word(publications, 'publications.docx')