#[PY-A05] Considere uma lista de números inteiros 
numeros = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

#Função map() para obter uma nova lista com o quadrado de cada número da lista numeros
quadrado = list(map(lambda x : x ** 2, numeros))
print(f"Os quadrados dos numeros usando map() são: {quadrado}")

#Função filter() para obter uma nova lista com números pares da lista numeros
pares = list(filter(lambda x : x % 2, numeros))
print(f"Os numeros pares usando filter() são {pares}")

#Função reduce()  para obter a soma de todos os números da lista numeros
from functools import reduce

soma = reduce(lambda x, y : x + y, numeros)
print(f"A soma dos numeros usando reduce() é {soma}")

