import os

#limpando terminal
os.system('cls')

#Lista que recebe os números
numbers = []

#loop para cadastrar os números
for i in range(10):
    number = int(input("Digite um número: "))
    numbers.append(number)
    os.system('cls')

#listas para separar impares e pares
impares = []
pares = []

#iteração para classificar os numeros nas listas
for x in numbers:
    if x % 2 == 1:
        impares.append((x))
    else:
        pares.append(x)

#ajuste das listas
numbers.clear()
impares = tuple(impares)
pares = tuple(pares)

#resultado final
print(f"Os números pares são: {pares} são {len(pares)} números e a soma é: {sum(pares)}")
print(f"Os numeros impares são: {impares} são {len(impares)} números e a soma é: {sum(impares)}")