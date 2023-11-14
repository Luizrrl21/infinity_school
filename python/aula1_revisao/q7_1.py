import os
import time

os.system('cls')

while True:
    contador = int(input("Digite a quantidade de segundos: "))
    if contador <= 0:
        os.system('csl')
        print("Inválido")
    else:
        break

while contador >= 0:
    if contador == 0:
        print("FIM")
    else:
        print(contador)
    contador = contador - 1
    time.sleep(1)