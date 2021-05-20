




class Book:
    language="english"
    def details(self,Library_name,book_name,author,pages):
        self.Library_name = Library_name
        self.book_name = book_name
        self.author = author
        self.pages = pages
    def printval(self):
        print("Libray_name",self.Library_name)
        print("book_name",self.book_name)
        print("author",Book.language)
bk=Book()
bk.details("skpottakadlibrary","thats the way we met","ravinder singh",295)
bk.printval()