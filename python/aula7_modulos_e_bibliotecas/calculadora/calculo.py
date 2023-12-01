from modulos import *

opcoes = ["+", "-", "*", "/"]

while True:
    n1 = float(input("Digite um número: "))
    acao = str(input("Ação: "))
    if acao not in opcoes:
        print("Erro!")
        continue
    n2 = float(input("Digite um número: "))
    if acao == "+":
        result = somar(n1,n2)
        print(result)
    elif acao == "-":
        result = subtrair(n1,n2)
        print(result)
    elif acao == "*":
        result = multiplicar(n1,n2)
        print(result)
    elif acao == "/":
        result = dividir(n1,n2)
        print(result)
    else:
        print("Erro")