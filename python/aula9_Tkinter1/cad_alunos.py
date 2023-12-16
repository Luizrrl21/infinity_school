lista_de_alunos = []

def adicionar_aluno():
    nome = str(input("Digite o nome: "))
    cpf = str(input("Digite o cpf: "))
    turma = str(input("Digite a turma: "))
    notas = []
    for i in range(4):
        nota = float(input("Digite uma nota: "))
        notas.append(nota)
    
    aluno = {
        "Nome" : nome,
        "CPF" : cpf,
        "Turma" : turma,
        "Notas" : notas

    }
    lista_de_alunos.append(aluno)

def visualizar_alunos():
    for aluno_atual in lista_de_alunos:
        print(f"""
        Nome do aluno: {aluno_atual["Nome"]}
        CPF do aluno: {aluno_atual["CPF"]}
        Turma do aluno: {aluno_atual["Turma"]}
        Notas do aluno: {aluno_atual["Notas"]}
""")

def deletar_aluno():
    visualizar_alunos()
    escolha = str(input("Digite o cpf do aluno que você quer deletar: "))
    for aluno_atual in lista_de_alunos:
        if escolha == aluno_atual["CPF"]:
            posicao_na_lista = lista_de_alunos.index(aluno_atual)
            lista_de_alunos.pop(posicao_na_lista)



while True:
    menu = int(input("""
    Escolha uma opção
    1 - Adicionar Aluno
    2 - Visualizar Alunos
    3 - Deletar Aluno
    0 - Sair
"""))
    
    match menu:
        case 1:
            adicionar_aluno()
        case 2:
            visualizar_alunos()
        case 3:
            deletar_aluno()
        case 0:
            break
        case _:
            print("Inválido")