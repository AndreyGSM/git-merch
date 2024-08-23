import random
numero_secreto = random.randint(1, 10)
intentos = 0

while True:
    intento = int(input('adivina el numero'))
    intentos = intentos+1
    if intento == numero_secreto:
        print(f"exito! tomo {intentos} intentos")
        break