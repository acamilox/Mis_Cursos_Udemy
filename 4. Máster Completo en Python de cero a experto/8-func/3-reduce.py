# importamos la libreria reduce
from functools import reduce

nums = [1, 2, 3, 4, 5, 6]
sum = reduce(lambda x, y: x + y, nums)
print(sum)

names = ['Andres Guzman', 'Pepe Doe', 'Mariela Gonzalez', 'Claudio Roe', 'James Gosling', 'Bruce Doe']
concat = reduce(lambda x, y: x + ', ' + y, names) # concatenacion de strings
total = reduce(lambda x, y: x + len(y), names, 0) # Se coloca el 0 para forzar a que sume los strings
print(concat)
print(total)