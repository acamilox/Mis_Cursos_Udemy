from .product import Product

class Item:
    def __init__(self,quantity: int, product: Product | None):
        self.__quantity = quantity
        self.__product = product

    #  Getters and Setters
    @property
    def quantity(self) -> int:
        return self.__quantity

    @quantity.setter
    def quantity(self, value: int):
        self.__quantity = value

    @property
    def product(self) -> Product | None:
        return self.__product

    @product.setter
    def product(self, value: Product | None):
        self.__product = value

    def calculate_amount(self):
        return self.quantity * self.product.price

    def __str__(self):
        return f'Item[quantity={self.quantity}, product={self.product}, self.calculate_amount={self.calculate_amount()}]'