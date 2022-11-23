from pymongo import MongoClient

class Phase2:
    def __init__(self):
        pass
    
    def print_gabagool(self):
        print(self.port)
    
    def handle_1(self):
        userInput = input("Enter keywords relating to an article to search for (Space seperated): ")
    
        if userInput == "EXIT":
            return
                
        if not userInput.isdigit():
            userInput = userInput.split(" ")
            userInput ='\"' + '\" \"'.join(userInput) + '\"'
            query = self.collection.find({"$text": {"$search": userInput}})
        else:
            query = self.collection.find({"year": int(userInput)})

        print("----------------------------------")

        count = 1
        results = False
        for x in query:
            results = True
            print("Result " + str(count))
            print("Id: " + x["id"])
            print("Title: " + x["title"])
            print("Year: " + str(x["year"]))
            print("Venue: " + x["venue"])
            print("----------------------------------")
            count += 1

        query.rewind()

        if not results:
            print("No results found.")
            return
        
        userInput = input("Enter a result to view more details, or EXIT to cancel: ")

        while True:
            if userInput == "EXIT":
                return
            if userInput.isdigit():
                if int(userInput) >= count:
                    userInput = input("Invalid entry. Please select a result or EXIT: ")
                else:
                    break
            else: 
                userInput = input("Invalid entry. Please select a result or EXIT: ")
        
        count = 1
        for y in query:
            if int(userInput) == count:
                id = y["id"]
                print("Id: " + id)
                print("Title: " + y["title"])
                print("Year: " + str(y["year"]))
                print("Venue: " + y["venue"])
                print("Authors: " + str(y["authors"]))
                try:
                    print("Abstract: " + y["abstract"])
                except:
                    print("No Abstract found.")
                print("----------------------------------")
                break
            else:
                count += 1

        query = self.collection.find({"references": id})

        print("References: ")

        for x in query:
            print(" Id: " + x['id'])
            print(" Title: " + x['title'])
            print(" Year: " + str(x['year']))
            print("----------------------------------")
        
        pass
    
    def handle_2(self):
       
        """
        handle_2 handles the user searching for authors in the database and selecting more
        information on them.
        """

        #Printing author notif:
        print("----------------------")
        print("Phase 2: Searching Authors")
        print("----------------------")
        
        userInput = input("Pleas enter a search keyword: ")

        #Checking if keyword is valid:
        if userInput is None:
            print("Invalid keyword!")
            return
        
        authorNames = set()

        #Checking the authors names that matched:
        for author in self.collection.find({"authors": {"$regex": ".*" + userInput + ".*" , "$options": 'i'}}):
            for name in author["authors"]:
                if userInput.lower() in name.lower():
                    authorNames.add(name)

        #Fecthing unique author names:
        authorNames = list(authorNames)
        # print(authorNames) #Testing please remove after:
            
        authorPublics = []

        #Fetching number of publications:
        matches = 0

        #Fetching all artists:
        authorPubs = self.collection.aggregate([{"$match": {"authors": {"$in": authorNames}}}, 
        {"$unwind": "$authors"}, 
        {"$match": {"authors": {"$in": authorNames}}}, 
        {"$group": {"_id": "$authors", "numOfPubs": {"$sum": 1}}}])

        authorPublics = list(authorPubs)

        matches = len(authorPublics)

        print("----------------------------------")
        for i in range(matches):
            displayName = authorPublics[i]["_id"]
            publications = authorPublics[i]["numOfPubs"]
            print("#" + str(i + 1) + " " + displayName + " publications: " + str(publications))
        print("----------------------------------")
        
        print()

        print("----------------------------------")
        userInput = input("Input a number listed above to view author info: ")
        print("----------------------------------")
    
        print()

        name = None
        if userInput.isnumeric() and 0 < int(userInput) and int(userInput) <= matches:
            userInput = int(userInput)
            name = authorPublics[userInput - 1]["_id"]

        #Fetching the artist info:
        authorInfo = self.collection.aggregate([{"$match": {"authors": name}},
         {"$unwind": "$authors"},
         {"$match": {"authors": name}},
         {"$sort": {"year": -1}}])

        authorInfo = list(authorInfo)
        for release in authorInfo:
            print("----------------------------------")
            print("Title: " + release["title"])
            print("Year: " + str(release["year"]))
            print("Venue: " + release["venue"])
            print("----------------------------------")
            print("\n")
        
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
        # self.port = input("Enter port: ")
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

