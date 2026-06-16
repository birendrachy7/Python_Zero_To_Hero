from typing import Optional
class Book:
    def __init__(self,id: int , title: str, author: str):
        self.id = id
        self.title = title
        self.author = author 
    def display(self):
        print("Book Id: ", self.id)
        print("Title: ", self.title)
        print("Author: ", self.author)

book1=Book(1,"Python","Birendra")
print(book1)
        