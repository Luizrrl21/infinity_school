import os

os.system('cls')

while True:
    tabuada = int(input("Digite um número: "))

    if tabuada > 0:
        os.system('cls')
        break
    else:
        print("Inválido")

print(f"A tabuada de {tabuada} é: ")
for i in range(1,11):
    print(f"por {i} = {tabuada*i}")