def menor_numero(*numeros):
    menor = numeros[0]
    for numero_atual in numeros:
        if numero_atual < menor:
            menor = numero_atual
    return menor

def maior_numero(*numeros):
    maior = numeros[0]
    for numero_atual in numeros:
        if numero_atual > maior:
            maior = numero_atual
    return maior

def media_numeros(*numeros):
    soma = 0
    for numero in numeros:
        soma += numero
    return soma / len(numeros)