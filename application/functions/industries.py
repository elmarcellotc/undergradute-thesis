# This script generates the uniques names for provinces and the uniques list for municipalities.
# This script also generate the uniques code for industries types.
import pandas as pd
import numpy as np
import os

os.chdir("..")

industries = pd.read_csv('treatement_data/industries.csv')

print(industries.columns)
industries = industries[['province_name_target', 'canton_name_target', 'province_name_source',
                         'canton_name_source', 'ciiu_4n4_target', 'ciiu_4n4_source']]

# generate uniques provinces

def uniques_txt(column_names, list_name, all_years=False, industries=industries):
    uniques_array = industries[column_names]
    uniques_array = uniques_array.to_numpy()

    uniques_array = np.unique(uniques_array)
    
    if all_years == True:
        uniques_array = in_all_years(column_names)
        

    with open(f'dictionaries/{list_name}.txt', 'w') as fp:
        for item in uniques_array:
            # write each item on a new line
            fp.write("%s\n" % item)
        print(f'{list_name} list done')
        
# Select, only those industry types with data for all years.

def in_all_years(column_names, industries=industries):
    None
        
if __name__ == '__main__':

    # Provinces name:
    column_names = ['province_name_target', 'province_name_source']
    list_name = 'provinces'
    uniques_txt(column_names, list_name)
    
    # Municipalities names
    column_names = ['canton_name_target', 'canton_name_source']
    list_name = 'municipalities'
    uniques_txt(column_names, list_name)
    
    # Products codes
    column_names = ['ciiu_4n4_target', 'ciiu_4n4_source']
    list_name = 'products'
    uniques_txt(column_names, list_name)