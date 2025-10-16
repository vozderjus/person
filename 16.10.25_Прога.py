class Book:
    def __init__(self, title, author, year):
        self.title = title
        self.author = author
        self.year = year

    def info(self) -> str:
        return f'{self.title}: Автор: {self.author}, Год издания: {self.year}'

class Ebook(Book):
    def __init__(self, title, author, year, format):
        self.title = title
        self.author = author
        self.year = year
        self.format = format
    
    
    def info(self) -> str:
        return f'{self.title}: Автор: {self.author}, Год издания: {self.year}, Формат: {self.format}'

book = Ebook('1984', 'Джордж Оруэлл', 'Хз', 'Йоу')
print(book.info())

