import os

alunos = []
opcoes = ["add","del","ver","sair"]

while True:
    acao = str(input("O que você deseja fazer? "))
    os.system('cls')
    #Ver alunos
    if acao == "ver":
        print(alunos)

    #Sair
    elif acao == "sair":
        break

    #Adicionar alunos
    elif acao == "add":
        add = {
            'matricula': str(input("Digite a matrícula do aluno: ")),
            'nome': str(input("Digite o nome do aluno: "))
        }
        alunos.append(add)
        print(f"Aluno {add['nome']} foi adicionado")

    #Deletar alunos
    elif acao == "del":
        matricula = str(input("Digite a matrícula do aluno que você quer excluir: "))
        for i in alunos:
            if i['matricula'] == matricula:
                alunos.remove(i)
                print(f"O aluno {i['nome']} foi removido")


    #Erro
    else:
        print(f"Erro! tente: {opcoes}")

    
    
