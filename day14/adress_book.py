class Book:
    def __init__(self,title,author,pages):
        self.title = title
        self.author = author
        self.pages = pages
    def display(self):
        print(f"Title:{self.title}, Author:{self.author}, Pages:{self.pages}")
book1=Book("Intro to python ","Eric methews",524)
book1.display()