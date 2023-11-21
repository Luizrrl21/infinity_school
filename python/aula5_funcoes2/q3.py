def maior(lista:list):
    maior = ""
    for i in lista:
        if len(i) > len(maior):
            maior = i
    return f"A maior palavra é {maior}"

lista = []

for i in range(5):
    palavra = str(input("Digite uma palavra: "))
    lista.append(palavra)

print(maior(lista))

