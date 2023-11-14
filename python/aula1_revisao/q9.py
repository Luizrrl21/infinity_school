import os

os.system('cls')
frase = str(input("Escreva uma frase: ")).upper()
contador_vogais = 0

for i in frase:
    if i in "AEIOUÁÓÍÚÉÃÕÂÊÎÔÛ":
        contador_vogais = contador_vogais + 1

print (f"A sua frase tem {contador_vogais} vogais")