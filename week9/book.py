class Book: 
    def __init__(self, title, year, language, author): 
        self.title = title
        self.year = year
        self.language = language
        self.author = author 
    
    def setTitle(self, title):
        self.title = title
    
    def setYear(self, year):
        self.year = year
    
    def setLanguage(self, language):
        self.language = language
    
    def setAuthor(self, author):
        self.author = author
    
    def getTitle(title):
        return title

    def getYear(year):
        return year

    def getLanguage(language):
        return language

    def getAuthor(author):
        return author