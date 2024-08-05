class Author:
    all_authors = []

    def __init__(self, name):
        if not isinstance(name, str) or not name:
            raise Exception("Name must be a non-empty string.")
        self.name = name
        self.contracts_list = []
        Author.all_authors.append(self)

    def contracts(self):
        return self.contracts_list  # [contract for contract in Contract.all_contracts if contract.author == self]

    def books(self):
        return list(set([contract.book for contract in self.contracts_list]))  # [contract.book for contract in self.contracts()]

    def sign_contract(self, book, date, royalties):
        contract = Contract(self, book, date, royalties)
        self.contracts_list.append(contract)
        book.contracts_list.append(contract)
        return contract
    
        #if not isinstance(book, Book):
        #    raise Exception("book must be an instance of the Book class.")
        #if not isinstance(date, str) or not date:
        #    raise Exception("date must be a non-empty string.")
        #if not isinstance(royalties, int) or royalties < 0 or royalties > 100:
        #    raise Exception("royalties must be an integer between 0 and 100.")
        #return Contract(self, book, date, royalties)

    def total_royalties(self):
        return sum(contract.royalties for contract in self.contracts_list)



class Book:
    all_books = []

    def __init__(self, title):
        if not isinstance(title, str) or not title:
            raise Exception("Title must be a non-empty string.")
        self.title = title
        self.contracts_list = []
        Book.all_books.append(self)

    def contracts(self):
        return self.contracts_list
    
    def authors(self):
        return list(set([contract.author for contract in self.contracts_list]))


class Contract:
    all_contracts = []

    def __init__(self, author, book, date, royalties):
        if not isinstance(author, Author):
            raise Exception("author must be an instance of the Author class.")
        if not isinstance(book, Book):
            raise Exception("book must be an instance of the Book class.")
        if not isinstance(date, str) or not date:
            raise Exception("date must be a non-empty string.")
        if not isinstance(royalties, int) or royalties < 0: # or royalties > 100
            raise Exception("royalties must be a non-negative integer")

        self.author = author
        self.book = book
        self.date = date
        self.royalties = royalties

        Contract.all_contracts.append(self)

    @classmethod
    def contracts_by_date(cls, date):
        return [contract for contract in cls.all_contracts if contract.date == date]
    
        #if not isinstance(date, str) or not date:
        #    raise Exception("date must be a non-empty string.")
        #return [contract for contract in cls.all_contracts if contract.date == date]
        