import json
from pymongo import MongoClient

# For this part, you will write a program, named load-json with a proper extension 
# (e.g. load-json.py if using Python), which will take a json file in the current directory
# and constructs a MongoDB collection. Your program will take as input a json file name and 
# a port number under which the MongoDB server is running, will connect to the server and will 
# create a database named 291db (if it does not exist). Your program then will create a collection named dblp.
#  If the collection exists, your program should drop it and create a new collection. 
# Your program for this phase ends after building the collection.

def main():

    port = input("Enter port: ")
    # client = MongoClient('mongodb://localhost:27012')
    client = MongoClient('mongodb://localhost:' + port)
    
    json_file = input("Enter JSON file: ")

    # TODO: do check, may not be needed
    db = client["291db"]

    collection = db["dblp"]
    collection.drop()
    # with open("dblp-ref-10.json") as f:
    with open(json_file, 'r') as f:
        # data = json.load(f.read())
        for line in f:
            data = json.loads(line)
            collection.insert_one(data)

if __name__ == "__main__":
    main()
