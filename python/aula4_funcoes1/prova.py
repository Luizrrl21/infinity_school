#[PY-A04] Desenvolva um programa em Python que permita ao usuário digitar várias notas.
#Em seguida, crie uma função chamada "calcular_media" que irá receber as notas digitadas e calcular a média do aluno. 
#Também crie uma função chamada "verificar_situacao" que, com base na média calculada, irá exibir a situação do aluno:
#"Reprovado" se a média for menor que 7, "Aprovado" se a média for maior ou igual a 7, e
#"Parabéns, sua média é 10" se a média for igual a 10.

import os

def media(lista: list):
    return round(sum(lista)/len(lista),2)

def situacao(valor: float):
    if valor == 10:
        return "Parabéns"
    if valor >= 7:
        return "Aprovado"
    if valor < 7:
        return "Reprovado"

notas = []
opcoes = ("add_nota", "verificar_situacao", "sair")

nome = str(input("Digite o nome do Aluno: "))

while True:
    choice = str(input("O que você deseja fazer? "))
    os.system('cls')
    if choice == "sair":
        break
    elif choice == "add_nota":
        nota = float(input("Digite a nota do Aluno: "))
        notas.append(nota)
        print(f"Nota adicionada ao aluno {nome}.")
    elif choice == "verificar_situacao":
        print(f"O aluno {nome} está com a média {media(notas)}. Situação: {situacao(media(notas))}")
    else:
        print(f"Erro! Tente digitar uma das opções: {opcoes}")



    
    
    
