from invoice.app.models.customer import Customer
from invoice.app.models.invoice import Invoice
from invoice.app.models.item import Item
from invoice.app.models.product import Product

# El resto de tu código se queda igual
customer = Customer("Andres", "Guzman", "12345678A")
print(f"Cliente creado: {customer.name}")

descripcion = input('Ingrese la descripción de la factura: ')
invoice = Invoice(descripcion, customer)

# Bucle para añadir 5 productos
for i in range(5):
    print(f"\n--- Añadiendo Producto {i + 1} ---")
    name = input('Ingrese el nombre del producto: ')
    price = float(input('Ingrese el precio del producto: '))
    product = Product(name, price)
    quantity = int(input('Ingrese la cantidad del producto: '))
    item = Item(quantity, product)
    invoice.add_item(item)


print("\n================== DETALLE DE LA FACTURA ==================")
print(invoice)