
# Dos instancias diferentes
x = [1,2,3]
y = [1,2,3]
z = x
print(x is y)
print(x is z)
print(z is y)
print(z is not y)

class Invoice:
    pass

# creación de los objetos distintos a y b
a = Invoice()
b = Invoice()
print(a is b)
print(a is not b)