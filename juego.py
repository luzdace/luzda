import random

intentos = 2
max_intentos = 3
num_random = random.randint(0,10)

print("Inicia ingresando un numero Que estoy pensando! - Numero de intentos 3")

while True:
    numero = int(input ("Que numero estoy pensando - Ingrese un numero: ") )
    if num_random == numero:
        break

    if intentos == max_intentos:
        print("juegos terminado: (")
        exit ()
        intetos += 1

    print ("Haz ganado")
