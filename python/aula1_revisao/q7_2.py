import os
import time

os.system('cls')

#Usando While

while True:
    contador = int(input("Digite a quantidade de segundos: "))
    if contador <= 0:
        os.system('csl')
        print("Inválido")
    else:
        break

for i in range (contador, -1, -1):
    
    if contador == 0:
        print("FIM")
    else:
        print(contador)
    contador = contador - 1
    time.sleep(1)