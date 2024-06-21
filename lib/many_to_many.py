class Author:
    all = []

    def __init__(self, name):
        if not isinstance(name, str):
            raise TypeError("Name must be a string")
        self.name = name

    def contracts(self):
        return [contract for contract in Contract.all if contract.author == self]
    
    def books(self):
        return [contract.book for contract in Contract.all if contract.author == self]
    
    def sign_contract(self, book, date, royalties, title):
        new_contract = Contract(self, book, date, royalties)
        new_book = Book(self, title)
    
    def total_royalties(self):
        roy_sum = 0
        roy_list = [contract.royalties for contract in Contract.all if contract.author == self]
        for roy in roy_list:
            roy_sum += roy
        return roy_sum



class Book:
    all = []

    def __init__(self, title):
        if not isinstance(title, str):
            raise TypeError("Title must be a string")
        self.title = title

    def contracts(self):
        return [contract for contract in Contract.all if contract.book == self]
    
    def authors(self):
        return [contract.author for contract in Contract.all if contract.book == self]


class Contract:
    all = []

    def __init__(self, author, book, date, royalties):
        self.author = author
        self.book = book
        if not isinstance(date, str):
            raise Exception("date should be a string")
        self.date = date
        if not isinstance(royalties, int):
            raise Exception("royalties should be an integer")
        self.royalties = royalties
        Contract.all.append(self)

    @property
    def author(self):
        return self._author
    
    @author.setter
    def author(self, author):
        if isinstance(author, Author):
            self._author = author
        else:
            raise Exception("author should be a member of the Author class.")

    @property
    def book(self):
        return self.book
    
    @book.setter
    def book(self, book):
        if not isinstance(book, Book):
            raise Exception("book should be a member of the Book class.")
        else:
            self._book = book

    @classmethod
    def contracts_by_date(cls, date):
        return [contract for contract in Contract.all if contract.date == date]