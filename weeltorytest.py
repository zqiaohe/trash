# -*- coding: utf-8 -*-
"""WeeltoryTest.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1fNUF4WflNcK8mJwpkhLWtfEqdMg-Iwhk
"""

import json
import os
import jsonschema 
import sys
import pandas as pd

schema_dir = "/content/drive/MyDrive/Honor/task_folder/schema/"
event_dir = "/content/drive/MyDrive/Honor/task_folder/event/"
schemas = os.listdir(schema_dir)
files = os.listdir(event_dir)

d = {'ErrorSchema': [], 'ErrorFileName': [], 'ErrorMessage': []}
df = pd.DataFrame(data=d)

for schemaname in schemas:
  with open(schema_dir+schemaname, 'r') as f:
    schema_file = f.read()
  schema = json.loads(schema_file)
  #print(schemaname)
  for filename in files:
    #print(filename)
    with open(event_dir+filename, 'r') as f:
      json_file = f.read()
    json_obj = json.loads(json_file)
    try:
      json_obj.fromkeys(schema.keys())
    except:
      row = [schemaname, filename, 'Empty file']
      df.loc[len(df)] = row
    
    try:
      jsonschema.validate(json_obj, schema)
    except:
      exc_type, exc_value, exc_traceback = sys.exc_info()
      row = [schemaname, filename, str(exc_value.message)]
      df.loc[len(df)] = row

df

print(df.to_html())