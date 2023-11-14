def maior(n1, n2):
    if n1 > n2:
        return n1
    elif n2 > n1:
        return n2
    else:
        return "São iguais"
numero1 = int(input("Digite o primeiro número: "))
numero2 = int(input("Digite o segundo número: "))

print(f"O maior número é {maior(numero1, numero2)}")