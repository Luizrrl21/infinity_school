def AdicionarAluno(lista: list):
    nome = str(input("Digite o nome: "))
    matricula = str(input("Digite a matricula: "))
    
    aluno = {
        "Nome" : nome,
        "Matricula" : matricula,
    }
    lista.append(aluno)
    print(f"\033[0;49;32mAluno(a) {nome} adicionado!\033[0;0m")

def VerAlunos(lista):
    if lista == []:
        print("\033[0;49;90mVázio, tente cadastrar alguém primeiro...\033[0;0m")
    else:
        for aluno_atual in lista:
            print(f"""\033[0;49;36m
            Nome do aluno: {aluno_atual["Nome"]}
            Matrícla: {aluno_atual["Matricula"]}
\033[0;0m""")

def RemoverAluno(lista):
    escolha = str(input("Digite a matrícula do aluno que você quer deletar: "))
    achou = False
    for i in lista:
        if escolha == i["Matricula"]:
            achou = True
            posicao_na_lista = lista.index(i)
            deletado = lista.pop(posicao_na_lista)
            print(f"\033[0;49;31mAluno {deletado['Nome']} deletado\033[0;0m")
    if achou == False:
        print("\033[0;49;33mERRO: Matrícula não localizada, tente novamente\033[0;0m")

def AtualizarAluno(lista):
    escolha = str(input("Digite a matrícula do aluno(a) que você quer editar: "))
    achou = False
    for i in lista:
        if escolha == i["Matricula"]:
            achou = True
            posicao_na_lista = lista.index(i)
            nome = str(input("Digite a alteração do Nome: "))
            lista[posicao_na_lista] = {
                "Nome" : nome,
                "Matricula" : escolha,
            }
            print(f"\033[0;49;32mNome do aluno(a) {escolha} alterado para {nome}\033[0;0m")
    if achou == False:
        print("\033[0;49;33mERRO: Matrícula não localizada, tente novamente\033[0;0m")