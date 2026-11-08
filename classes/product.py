class Product():
    def __init__(self ,name ,price , quantity = 0):
        self._name =name
        self._quantity = quantity
        self.__price = price
        self.total_value = quantity*price

    @property
    def price(self):
        return self.__price


    @property
    def name(self):
        return self._name
    @property
    def quantity(self):
        return self._quantity
    
    @price.setter
    def price(self ,val):
        if val < 0 :
           raise ValueError("price must be positive")
        self.__price = val


    def add_stock(self , quantity):
        if quantity < 0:
             raise ValueError("quantity must be > 0")
        self._quantity += quantity

    def sell(self , amount):
        if  amount < 0:
            raise ValueError("amount must be positive")
        self._quantity -= amount
        

    def __str__(self):
        return f'{self.name}:{self.price} * {self.quantity} = {self.total_value}'


    def __repr__(self):
        return f'{self.name}:{self.price} * {self.quantity} = {self.total_value}'
