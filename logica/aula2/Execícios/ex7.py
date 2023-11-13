n1 = float(input("Digite o primeiro número: "))
n2 = float(input("Digite o segundo número: "))
n3 = float(input("Digite o terceiro número: "))

if n1 > n2 and n1 > n3:
    print(f"{n1} é o maior número")
elif n2 > n1 and n2 > n3:
    print(f"{n2} é o maior número")
elif n3 > n1 and n3 > n2:
    print(f"{n3} é o maior número")
else:
    print("Os maiores números tem valores iguais, impossível definir o maior")

if n1 < n2 and n1 < n3:
    print(f"{n1} é o menor número")
elif n2 < n1 and n2 < n3:
    print(f"{n2} é o menor número")
elif n3 < n1 and n3 < n2:
    print(f"{n3} é o menor número")
else:
    print("Os menores números tem valores iguais, impossível definir o menor")