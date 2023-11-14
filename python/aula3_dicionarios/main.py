import os

alunos = []

while True:
    os.system('cls')
    nome = str(input("Digite o nome do aluno: "))
    if nome == "fim":
        break
    nota = float(input("Digite a nota do aluno: "))
    if nota >= 0 and nota <=10:
        alunos.append([nome, nota])
    else:
        print("Digite uma nota válida de 0 a 10")

maior_nota = 0
melhor_aluno = []

for aluno in alunos:
    if aluno[1] >= maior_nota:
        maior_nota = aluno[1]
        melhor_aluno.append(aluno[0])

print(f"A maior nota é {maior_nota} alcançada por: {melhor_aluno}")
