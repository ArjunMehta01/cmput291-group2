from pymongo import MongoClient

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
        pass
    


    # The user should be able to add an article to the collection by providing a unique id, 
    # a title, a list of authors, and a year. The fields abstract and venue should be set to null, 
    # references should be set to an empty array and n_citations should be set to zero.

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
        
        year = int(input("Enter year_ "))
        while(year < 0):
            year = (input("year must be above 0. Please enter a new year or EXIT to return to menu._ "))
            if id == "EXIT":
                return
        
        # TODO: verify None is null
        dict_document = {
            "abstract": None,
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

