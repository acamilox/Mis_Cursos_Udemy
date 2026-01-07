from datetime import datetime
from typing import Optional, List
from .customer import Customer
from .item import Item

class Invoice:
    __last_folio = 0
    def __init__(self, description: str, customer: Optional[Customer]):
        Invoice.__last_folio += 1
        self.__folio_id = Invoice.__last_folio

        self.__date = datetime.now()
        self.__description = description
        self.__customer = customer
        self.__items: List[Item] = []

    @property
    def folio_id(self):
        return self.__folio_id

    @property
    def date(self):
        return self.__date

    @property
    def customer(self):
        return self.__customer

    @customer.setter
    def customer(self, value):
        self.__customer = value

    @property
    def items(self):
        return self.__items

    @items.setter
    def items(self, value):
        self.__items = value

    @property
    def description(self):
        return self.__description

    def add_item(self, item: Item) -> 'Invoice':
        self.__items.append(item)
        return self

    def calculate_total(self) -> float:
        total = 0.0
        for item in self.items:
            total += item.calculate_amount()
        return total

    def __str__(self) -> str:
        # Encabezado
        detail = f'--- FACTURA N°: {self.folio_id} ---\n'
        detail += f'Fecha: {self.date.strftime("%d/%m/%Y")}\n'
        detail += f'Descripción: {self.description}\n\n'

        # Detalles del cliente
        customer_name = f'{self.customer.name} {self.customer.last_name}'
        detail += f'--- Cliente ---\n'
        detail += f'Nombre: {customer_name}\n'
        detail += f'NIF: {self.customer.tax_id}\n\n'

        # Detalles de los items
        detail += f'--- Detalle de Productos ---\n'
        detail += f'{"Producto":<20} {"Precio":>10} {"Cantidad":>10} {"Subtotal":>10}\n'
        detail += f'{"-" * 20:<20} {"-" * 10:>10} {"-" * 10:>10} {"-" * 10:>10}\n'
        for item in self.items:
            detail += f'{item.product.name:<20} ${item.product.price:>9.2f} {item.quantity:>10} ${item.calculate_amount():>9.2f}\n'

        # Total
        detail += f'\n{"GRAN TOTAL:":>42} ${self.calculate_total():>9.2f}\n'
        detail += f'----------------------------------------------------------'

        return detail