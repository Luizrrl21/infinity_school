numero = int(input("Digite um número: "))

verifica = lambda numero : f"{numero} é par" if numero % 2 == 0 else f"{numero} é impar"

print(verifica(numero))