
from .product import Product


class Inventory():
    def __init__(self  ):
        self._products = []


    @property
    def products(self):
        return self._products    
    
    def add(self ,product):
        if type(product) == Product:
            if product  in self.products:
                raise ValueError("this object allready exsist")
            self._products.append(product)

    def find(self , name):
        for p in self.products:
            if p.name == name:
                return p
        return None            

    def by_value(self):
       return sorted(self.products, key=lambda p: p.total_value , reverse = True)