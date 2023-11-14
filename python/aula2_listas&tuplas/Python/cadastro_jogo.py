import os

os.system('cls')

lista = []

jogadores = int(input("Digite quantos jogadores vão participar: "))

while len(lista) < jogadores -1:
    pessoa = str(input("Digite o nome de um jogador: "))
    lista.append(pessoa)

impostor = str(input("Digite o nome do impostor: "))
while True:
    posicao = int(input("Digite a posição do Impostor: "))
    if posicao > len(lista)+1 or posicao <= 0:
        print("Posição inválida, tente novamente!")
    else:
        i = posicao-1
        lista.insert(i, impostor)
        break


print(lista)