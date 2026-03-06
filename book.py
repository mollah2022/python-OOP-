class Book:

    def __init__(self,name,author):
        self.name = name
        self.author = author
        self.price = 0

    
    def set_price(self,price):
        self.price = price

    def get_price(self):
        return self.price
    
    def view(self):
        print("Book Name ",self.name)
        print("Author Name ",self.author)
        print("Book Price ",self.price)

    
        