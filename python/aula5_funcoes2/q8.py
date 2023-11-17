verifica = lambda numero : "Dívisivel" if numero % 3 == 0 and numero % 5 == 0 else "Não divisível"

while True:
    n1 = float(input("Digite um número: "))
    print(verifica(n1))