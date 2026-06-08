class Book:
    def __init__(self, title, author):
        self.title = title
        self.author = author

    def show_info(self):
        print(f"Book: {self.title} by {self.author}")


class EBook(Book):
    def __init__(self, title, author, file_size):
        super().__init__(title, author)
        self.file_size = file_size


    def show_info(self):
        print(f"E-Book: {self.title} by {self.author}, Size: {self.file_size} MB")


class PrintedBook(Book):
    def __init__(self, title, author, no_of_page):
        super().__init__(title, author)
        self.no_of_page = no_of_page


    def show_info(self):
        print(f"Printed Book: {self.title} by {self.author}, Pages: {self.no_of_page}")
    
    
    def __add__(self,other):
        return PrintedBook(self.title+ other.title+ ","+self.no_of_page+other.no_of_page)

books = [
    EBook("Python", "ABC", 21),
    PrintedBook("Java", "BCD", 1500),
    EBook("JAva","Xyz",20),
    PrintedBook("C","DFG",100)
]

for book in books:
    book.show_info()
    
print("#---------------#")

book=books[1]+books[3]
print(book)
