import os
import pandas as pd
from pymongo import MongoClient
import json
import csv
import os.path
import glob


folder = 'Excel_path'
file_list = []

for (paths, dirs, files) in os.walk(folder):
    for file in files:
        if file.endswith(".xlsx"):
            file_list.append(os.path.join(paths, file))

            
all_data = pd.DataFrame()
for file in file_list:
    read_file = pd.read_excel (file)
    all_data = all_data.append(read_file,ignore_index=True)

aadharData = all_data.to_csv(r'aadhar_data.csv',index = None, header=True)


MONGODB_URI = "mongodb://127.0.0.1:27017/"
client = MongoClient(MONGODB_URI)

db = client["aavas_aadhar"]
aadhar_data = db["aadhar_data"]

data = pd.read_csv('aadhar_data.csv')
payload = data.to_json(orient='records')
aavas_aadhar_data = json.loads(payload)
for doc in aavas_aadhar_data:
    aadhar_data.insert_one(doc)