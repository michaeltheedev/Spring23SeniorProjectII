import pandas as pd
import os
import json

#Enter path to JSON files
path = "Path to JSON Directory"

#Change the directory

os.chdir(path)

#Read JSON File

def read_json_file(file_path):
    with open(file_path,'r') as f:
        data = json.loads(f.read())

        #Create data frame only containing specfied fields below
        #Current error: Record path key "title" is not being detected, have to debug why.
        df_nested_list = pd.json_normalize(data,record_path="title",meta=[['primaryTaxonomyNodes','title'],['primaryTaxonomyNodes','definition'],'benefits','description'],errors='ignore')
        
        #Display dataframes to check if only specified fields are contained.
        display(df_nested_list)

#Iterate through all JSON files
for file in os.listdir():
    if file.endswith('.json'):
        file_path = f"{path}\{file}"

        #call and read JSON file function
        read_json_file(file_path)

