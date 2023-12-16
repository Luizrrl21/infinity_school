from funcoes import *

bd = []

while True:
    try:
        menu = int(input("""
        Escolha uma opção
        1 - Adicionar Aluno
        2 - Remover Aluno
        3 - Atualizar Aluno
        4 - Ver Alunos
        0 - Sair
    """))
    
        match menu:
            case 1:
                AdicionarAluno(lista=bd)
            case 2:
                RemoverAluno(lista=bd)
            case 3:
                AtualizarAluno(lista=bd)
            case 4:
                VerAlunos(lista=bd)
            case 0:
                print("\033[0;49;36mAté a próxima! ;)\033[0;0m")
                break
            case _:
                print("\033[0;49;31mNúmero inválido\033[0;0m")
    except:
        print("\033[0;49;31mDigite um número!\033[0;0m")