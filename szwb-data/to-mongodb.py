import pymongo
import json
from pymongo import MongoClient, InsertOne
from tqdm import tqdm

client = pymongo.MongoClient('mongodb://hanx:admins@10.64.68.30/')
db = client.szwb
collection = db.record
requesting = []

with open(r"szwb-data\json\szwb-delist.json", encoding='UTF-8') as f:
    
    myDict = json.load(f)
    for myRecord in tqdm(myDict):
        requesting.append(InsertOne(myDict[myRecord]))

result = collection.bulk_write(requesting)
client.close()