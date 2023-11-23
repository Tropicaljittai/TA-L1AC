class Library: 
    Book = []
    Author = []

    def addAuthor(self, author):
        self.Author.append(author)

    def removeAuthor(self, id):
        for author in self.Author: 
            if author.id == id:
                self.Author.remove(author)
                break

        print(f"Your id {id} not found")

    def printAuthor(self, id):
        for author in self.Author: 
            if author.id == id:
                print(f"Name: {author.name} - email: {author.email}")
                return
        
        print(f"Your id {id} not found")
        
    # printAllAuthors 
    # addBook
    # removeBook based on the id 
    # printBook based on the id 
    # printAllBooks