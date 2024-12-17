class library:
    def __init__(self):
        self.nobook = 0
        self.books = []

    def addbooks(self,book):
        self.books.append(book)
        self.nobook = len(self.books)
    
    def show(self):
        print(f"the number of books are {self.nobook}")
        for book in self.books:
            print(book)

l1 = library()
l1.addbooks("Harry Potter1")
l1.addbooks("Harry Potter2")
l1.addbooks("Harry Potter3")
l1.addbooks("Harry Potter4")
l1.addbooks("Harry Potter5")
l1.show()