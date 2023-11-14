#QUESTÃO 1
#Dado o conjunto Cores com a seguinte estrutura {"Amarelo", "Azul", "Vermelho", "Verde"}
#faça um programa que peça uma cor ao usuário e guarde essa cor em uma lista, o programa
#pedirá cores ao usuário até ele digitar a palavra chave "sair", quando o usuário sair do programa faça ele inserir todas as cores da lista dentro do conjunto
#e depois mostrar o conjunto na tela

import os

cores = {"Amarelo", "Azul", "Vermelho", "Verde"}
novas_cores = []

while True:
    os.system('cls')
    cor = str(input("Escolha uma cor: "))
    if cor == "sair":
        break
    novas_cores.append(cor)

cores.update(novas_cores)
print(cores)