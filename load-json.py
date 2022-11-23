import json
from pymongo import MongoClient
from phase2 import Phase2
import time


def phase1():
    start_time = time.time()
    print("PHASE 1")
    print("----------------------")
    port = input("Enter port: ")
    client = MongoClient('mongodb://localhost:' + port)
    
    json_file = input("Enter JSON file: ")

    db = client["291db"]
    collection = db["dblp"]

    collection.drop()
    with open(json_file, 'r') as f:
        for line in f:
            data = json.loads(line)
            collection.insert_one(data)
    collection.create_index([('title', 'text'),('authors', 'text'), ('abstract', 'text'), ('venue', 'text'), ('references', 'text')])
    print("--- %s seconds ---" %(time.time() - start_time))

if __name__ == "__main__":
    print("Setting Up MongoDB Server")
    phase1()
