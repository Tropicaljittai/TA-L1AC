from author import Author
from library import Library
from book import Book

lib = Library()

au1 = Author("JK Rowling", "rowling@gmail.com")

lib.addAuthor(au1)
lib.printAuthor(au1.id)