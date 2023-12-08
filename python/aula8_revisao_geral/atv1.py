lista = []

while True:
    numero = int(input("Digite um número inteiro: "))
    lista.append(numero)
    acao = str(input("Deseja continuar? "))
    if acao == "n":
        break


pares = list(filter(lambda x: True if x % 2 == 0 else False, lista))

print(pares)