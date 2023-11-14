import os

os.system("cls")

n1 = float(input("Digite um número: "))
n2 = float(input("Digite outro número: "))

while True:
    op = str(input("Qual operação você vai fazer: "))
    simbolos = ["+","-","*","/"]

    if op not in simbolos:
        print("Operador inválido, tente novamente!")
    else:
        break

os.system("cls")

if op == "+":
    total = n1 + n2
elif op == "-":
    total = n1 - n2
elif op == "*":
    total = n1 * n2
elif op == "/":
    total = n1 / n2

if total == 0:
    print(f"Igua a 0, que é um número neutro")

if total > 0:
    condicao = "Positivo"
else:
    condicao = "Negativo"

if total % 2 == 0 and float(total) == int(total) and total > 0:
    i_ou_p = "e Par"
elif total % 2 == 1 and float(total) == int(total) and total > 0:
    i_ou_p = "e Ímpar"
else:
    i_ou_p = "e não é natural!"

print(f"O total é {total}, é um número {condicao} {i_ou_p}")