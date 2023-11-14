notas = []

while len(notas) < 4:
    valor = float(input("Digite uma nota: "))
    if valor < 0 or valor > 10:
        print("Valor inválido")
    else:
        notas.append(valor)

media = sum(notas)/len(notas)

if media == 10:
    print(f"Aprovado com Distinção (média {media})")
elif media >=7:
    print(f"Aprovado (média {media})")
else:
    print(f"Reprovado (média {media})")