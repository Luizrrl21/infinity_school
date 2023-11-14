lista = []

for i in range(5):
    fruta = str(input("Escolhe uma fruta: "))
    lista.append(fruta)

lista[2] = "Melancia"
print(lista)