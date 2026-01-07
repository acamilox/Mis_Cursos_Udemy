
print('=======================================================While')
i = 0
while i<=5:
    print(f'Contador es {i}')
    i +=1


print('=======================================================While listas')
names = ['Andres','luna','Juan','Margarita']
count = 0
while count < len(names):
    print(f'Nombres en posicion {count}: {names[count]}')
    count+=1

print('======================================================= do while ejemplo práctico')
correct_number = 7

while True:
    attempt = int(input('Adivina el numero: '))
    if attempt == correct_number:
        print('Correcto! has adivinado el numero!')
        break
    else:
        print('Incorrecto, intenta de nuevo!')