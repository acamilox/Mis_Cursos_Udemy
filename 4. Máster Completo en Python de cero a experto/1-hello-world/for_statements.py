for i in range(5):
    print(i)

print('============== inica en dos e incrementa en 2')
for element in range(0,10,2):
    print(element)


print('============== decremento')
for i in range(10,0,-1):
    print(i)


print('============== decremento')
for i in range(10,-1,-1):
    print(i)


print('============== iterar un list')
names = ['Andres','Pepe','Jhon','Juan','1000', '3.1415']
for name in names:
    print(name)


print('============== iterar string name')
for name in names:
    print(name)
    for char in names:
        print(char)


print('============== iterar string email')
email = 'andres.correo@hotmail.com'
for c in email:
    print(c)