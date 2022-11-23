import json
from pymongo import MongoClient
from phase2 import Phase2
import time


# TODO: checking if valid
def phase1():
    start_time = time.time()
    print("PHASE 1")
    print("----------------------")
    port = input("Enter port: ")
    client = MongoClient('mongodb://localhost:27012')
    client = MongoClient('mongodb://localhost:' + port)
    
    json_file = input("Enter JSON file: ")

    # TODO: do check, may not be needed
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
    phase1()
    test = Phase2()
    test.run()

