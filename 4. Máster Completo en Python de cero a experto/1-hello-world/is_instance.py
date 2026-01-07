class Person:
    pass

class Animal: # Clase padre
    pass

class Dog(Animal): # herencia de la clase padre llamada Animal
    pass

num = 10
text = 'Creando un objeto de la clase str'
num_decimal = 3.1415

b1 = isinstance(text, str) # objeto, tipo de dato
print(f'txt es del tipo str = {b1}')

b2 = isinstance(num, int)
print(f'num es del tipo int = {b2}')

b3 = isinstance(num_decimal, float)
print(f'{num_decimal} es del tipo float = {b3}')

b4 = isinstance(num, str)
print(f'{num} es del tipo str? = {b4}')

b5 = isinstance(b4, bool)
print(f'{b4} es del tipo bool? = {b5}')

data = 3.14
b6 = isinstance(data, (int, float))
print(f'{data} es del tipo int o float? = {b6}')

b7 = isinstance(text, (int, float))
print(f'{text} es del tipo int o float? = {b7}')