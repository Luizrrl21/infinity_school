numero1 = float(input("Digite um número: "))
numero2 = float(input("Digite outro número: "))

if numero1 > numero2:
    print(f"{numero1} é o maior número")
elif numero1 == numero2:
    print(f"Os números são iguais")
else:
    print(f"{numero2} é o maior número")