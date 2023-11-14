def imc(peso: float, altura: float):
    return round(peso/altura**2,2)

lista_imc = []

for i in range(4):
    peso = float(input("Digite o Peso: "))
    altura = float(input("Digite a altura: "))
    lista_imc.append(imc(peso, altura))

print(lista_imc)