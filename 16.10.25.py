class Book:
    def __init__(self, title, author, year):
        self.title = title
        self.author = author
        self.year = year
    def info(self) -> str:
        return f'{self.title}: Автор: {self.author}, Год издания: {self.year}'

book = Book('1984', 'Джордж Оруэлл', 'Хз')
print(book.info())
