n1 = float(input("Digiteum número: "))

verifica = lambda numero : numero if numero > 10 else numero / 2

print(verifica(n1))