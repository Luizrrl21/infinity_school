numero1 = int(input("Digite um número: "))
numero2 = int(input("Digite outro número: "))

lista = []

for i in range(numero1+1, numero2):
    lista.append(i)

print(f"Os números que estão entre {numero1} e {numero2} são: {lista}")