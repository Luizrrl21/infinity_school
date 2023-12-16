from escola.matematica import *
from escola.portugues import *

lista = []
for i in range(4):
    nota = float(input("Digite uma nota: "))
    lista.append(nota)

print(f"O maior número é {maior_numero(lista)}")
print(f"O menor número é {menor_numero(lista)}")
print(f"A média dos números é {media_numeros(lista)}")