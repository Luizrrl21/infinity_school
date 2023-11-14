import os

os.system('cls')
frase = str(input("Escreva uma frase: ")).upper()
count_vogais = 0
count_consoante = 0

for i in frase:
    if i in "AEIOUÁÓÍÚÉÃÕÂÊÎÔÛ":
        count_vogais = count_vogais + 1
    elif i in "BCDFGHJKLMNPQRSTVWXYZ":
        count_consoante = count_consoante + 1

print(f"A sua frase tem {count_vogais} vogais e {count_consoante} consoantes")