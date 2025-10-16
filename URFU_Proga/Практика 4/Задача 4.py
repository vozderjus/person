from datetime import datetime
from abc import ABC, abstractmethod

class Printable(ABC):
    @abstractmethod
    def print_info(self):
        pass


class Book(Printable):
    def __init__(self, title, author, year):
        self.title = title
        self.author = author
        self.year = year

    def __eq__(self, other):
        return isinstance(other, Book) and (self.title == other.title or self.year == other.year)

    def info(self) -> str:
        return f'{self.title}: Автор: {self.author}, Год издания: {self.year}'
    
    def print_info(self):
        return self.info()
    
    def __str__(self):
        return self.info()
    
    @classmethod
    def from_string(cls, data):
        title, author, year = data.split(';')
        return cls(title, author, int(year))
    
    @property
    def age(self):
        return datetime.now().year - self.year
    
    @age.setter
    def age(self, value):
        self.year = datetime.now().year - value
    

book1  = Book.from_string("1984;Оруэлл;1949")
book2 = Book.from_string("1983;Кто-то;1949")
print(book1.age)
print(book1 == book2)
print(book1.print_info())
