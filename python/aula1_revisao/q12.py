import os

lista = []

os.system('cls')
while True:
    prod = str(input("Produto: "))
    if prod == "FIM":
        print(f"Valor total a pagar é R$ {round(sum(lista),2)}")
        break
    else:
        preco = float(input("Valor: "))
        os.system('cls')
        lista.append(preco)