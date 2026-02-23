import random
numero = random.randint(1, 10)
adivinacion = 0
intentos = 0
while adivinacion != numero:
    print('Adivina el número del 1 al 10')
    try:
        adivinacion = int(input())
    except ValueError:
        print('El valor debe de ser un número')
        continue
    intentos += 1
    if adivinacion < 1:
        print('El número debe de ser mayor o igual a 1')
    elif adivinacion > 10:
        print('El número debe ser menor o igual que 10')
    elif adivinacion != numero:
        print('Casi lo logras, vuelve a intentarlo')
print(f'Felicidades lo lograste en {intentos}')