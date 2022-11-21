from pymongo import MongoClient
from heapq import nlargest

class Phase2:
    def __init__(self):
        pass
    
    def print_gabagool(self):
        print(self.port)
    
    def handle_1(self):
        pass
    
    def handle_2(self):
        pass
    
    
    def handle_3(self):
        try:
            n = int(input("Enter a value of n_ "))
            while(n < 0):
                n = input("n must be 0 or greater. Please enter a new n or EXIT to return to menu._ ")
                if n == "EXIT":
                    return
        except:
            print("must be integer >= 0")
            return

        # get top n venues
        # TODO: change such that count / sort by number referencing venue
        venue_pipeline = [
            { "$project": { "_id": 0,  "id": 1, "venue": 1} }

        ]

        pipeline = [
            # $match EXCLUDES empty string -> may be unneeded
            { "$unwind" : "$references" },
            { "$project": { "references": 1} }        
        ]

        # TODO: determine if we leave out '' venue
        venuePipe = self.collection.aggregate(venue_pipeline)
        referencePipe = self.collection.aggregate(pipeline)
        
        all_references = {}
        id_venue = {}
        # maxi = 0

        for mem in venuePipe:
            if mem["id"] not in id_venue.keys():
                id_venue[mem["id"]] = mem['venue']

        for mem in referencePipe:
            if mem["references"] not in all_references.keys():
                all_references[mem["references"]] = 1
            else:
                all_references[mem["references"]] += 1

        res = nlargest(n, all_references, key = all_references.get)
        print(res)
        print("whore")
        
    def handle_4(self):
        id = input("Enter Unique id_ ")

        while(self.collection.count_documents({'id': id}) > 0):
            id = input("id already exists. Please enter a new id or EXIT to return to menu._ ")
            if id == "EXIT":
                return
                

        title = input("Enter title_ ")
        author_list = []

        while(True):
            new_author = input("Enter name of new author or 'EXIT' to stop adding authors_ ")
            if new_author == "EXIT":
                break
            else:
                author_list.append(new_author)
        while(True):
            try:
                year = int(input("Enter year_ "))
                while(year < 0):
                    year = (input("year must be above 0. Please enter a new year or EXIT to return to menu._ "))
                    if id == "EXIT":
                        return
                break
            except:
                print("year must be a number")
                return
        
        # TODO: verify None is null
        dict_document = {
            "abstract": "",
            "authors": author_list,
            "n_citation": 0,
            "references": [],
            "title": title,
            "venue": None,
            "year": year,
            "id": id
        }
        self.collection.insert_one(dict_document)



    def run(self):
        self.port = input("Enter port: ")
        client = MongoClient('mongodb://localhost:27012')
        # client = MongoClient('mongodb://localhost:' + port)

        self.db = client["291db"]
        self.collection = self.db["dblp"]

        while(True):
            print("Choose from the following options:")
            print("1. Search for articles")
            print("2. Search for authors")
            print("3. List the venues")
            print("4. Add an article")
            print("5. Exit")
            choice = input("Enter Choice_ ")

            if(choice == "1"):
                self.handle_1()
            elif(choice == "2"):
                self.handle_2()
            elif(choice == "3"):
                self.handle_3()
            elif(choice == "4"):
                self.handle_4()
            elif(choice == "5"):
                print("Exiting system!")
                break
            else:
                print("Invalid choice. Please choose again.")

