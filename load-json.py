import json
from pymongo import MongoClient
from phase2 import Phase2


# TODO: checking if valid
def phase1():
    print("PHASE 1")
    print("----------------------")
    port = input("Enter port: ")
    client = MongoClient('mongodb://localhost:27012')
    # client = MongoClient('mongodb://localhost:' + port)
    
    json_file = input("Enter JSON file: ")

    # TODO: do check, may not be needed
    db = client["291db"]

    collection = db["dblp"]
    collection.drop()
    with open("dblp-ref-10.json") as f:
    # with open(json_file, 'r') as f:
        # data = json.load(f.read())
        for line in f:
            data = json.loads(line)
            collection.insert_one(data)
    

if __name__ == "__main__":
    phase1()
    test = Phase2()
    test.run()

