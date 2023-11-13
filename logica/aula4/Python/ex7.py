numeros = []

while len(numeros) < 5:
    numero = float(input("Digite um número: "))
    numeros.append(numero)

print(f"O maior número é {max(numeros)}")

