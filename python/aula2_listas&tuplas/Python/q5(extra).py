# EXTRA:
# FAÇA UM PROGRAMA QUE PEDE PARA O USUÁRIO CADASTRAR 5 ALUNOS
# COM NOME E NOTA, E NO FINAL MOSTRA O NOME E NOTA DO ALUNO QUE TIROU A MAIOR NOTA

import os
os.system('cls')
alunos = []
notas = []
quantidade = float(input("Digite a quantidade de alunos: "))
os.system('cls')

while len(alunos) < quantidade:
    nome = str(input(f"Digite o nome do {len(alunos)+1}° aluno: "))
    nota = float(input(f"Nota do {nome}: "))
    alunos.append([nome, nota])
    notas.append(nota)
    os.system('cls')

maior = max(notas)

for i in alunos:
    if i[1] == maior:
        print(f"A maior nota foi do {i[0]} ({i[1]})")
