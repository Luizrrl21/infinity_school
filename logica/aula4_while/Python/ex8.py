numeros = []

while len(numeros) < 5:
    numero = float(input("Digite um número: "))
    numeros.append(numero)

print(f"A soma é {sum(numeros)} e a média é {sum(numeros)/5}")