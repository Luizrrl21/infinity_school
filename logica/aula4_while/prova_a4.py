# [LP-A04] Escreva um programa em python que leia números inteiros do teclado.
#O programa deve ler os números até que o usuário digite 0 (zero).
#No final da execução, exiba a quantidade de números digitados, assim como a soma e a média aritmética.

numeros = []

while True:
    numero = int(input("Digite um número: "))
    if numero == 0:
        break
    else:
        numeros.append(numero)

qtd = len(numeros)
soma = sum(numeros)
media = soma/qtd

print (f"Foram digitados {qtd} números, a soma é {soma} e a média é {media}")