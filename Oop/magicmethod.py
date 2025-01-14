# Magic methods = Dunder methods (double underscode) __init__ , __str__,__eq__
#                 They are automatically called by many of Python built-in operations
#                 They allow developers to define or costumize the behavior of objects
from matplotlib.pyplot import title


class Student:
    def __init__(self,name,gpa):
        self.name = name
        self.gpa = gpa
    #Muda o comportamento quando chama o objeto
    def __str__(self):
        return f"name: {self.name} gpa: {self.gpa}"

    def __eq__(self,other):
        return self.name == other.name

    def __gt__(self, other):
        return self.gpa > other.gpa



class Book:
    def __init__(self,title,author,num_pages):
        self.title = title
        self.author = author
        self.num_pages = num_pages

    def __str__(self):
        return f"'{self.title}' by {self.author}"

    def __eq__(self, other):
        return self.title == other.title and self.author == other.author

    def __lt__(self, other):
        return self.num_pages < other.num_pages

    def __add__(self, other):
        return f"{self.num_pages + other.num_pages}"

    def __contains__(self, items):
        return items in self.title or items in self.author

    def __getitem__(self, item):
        if item == "title":
            return self.title
        elif item == "author":
            return self.author
        elif item == "num_pages":
            return self.num_pages
        else:
            return f"{item} não foi encontrado"


book1 = Book(title="Hobbit",author="J.R.R Tolkien",num_pages=310)
book2 = Book(title="Hobbit",author="J.R.R Tolkien",num_pages=300)
book3 = Book(title="Harry Potter",author="J.K Rowling",num_pages=223)
#__str__
print(book1)
#__eq__
print(book1 == book2)
#lt
print(book1 < book3)

print("Hobbit" in book1)
#getitem
print(book3["title"])
