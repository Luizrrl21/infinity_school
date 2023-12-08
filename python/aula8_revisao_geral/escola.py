bd = []

while True:
    print("""
    1 - Cadastrar aluno
    2 - Visualizar Alunos
    3 - Deletar Aluno
    4 - Sair
    """)

    acao = int(input("Escolha a opção:"))

    #sair
    if acao == 4:
        print("Até logo!")
        break
    #add
    elif acao == 1:
        nome = str(input("Nome: ")).upper()
        while True:
            try:
                cpf = str(input("CPF: "))
                break
            except:
                print("Digite um CPF Válido!")
        turma = str(input("Turma: "))
        notas = []
        contador = 1
        while True:
            try:
                if contador == 5:
                    break
                else:
                    valor = float(input(f"Digite a {contador}º nota:"))
                    contador += 1
                    notas.append(valor)
            except:
                print("Digite uma nota válida!")
                continue
        
        dicionario = {
            "nome" : nome,
            "cpf" : cpf,
            "turma" : turma,
            "Nota1" : notas[0],
            "Nota2" : notas[1],
            "Nota3" : notas[2],
            "Nota4" : notas[3]
        }
        bd.append(dicionario)
    #view
    elif acao == 2:
        for i in bd:
            print(f"""
            Nome: {i["nome"]}
            CPF: {i["cpf"]}
            Turma: {i["turma"]}
            Nota 1: {i["Nota1"]}
            Nota 2: {i["Nota2"]}
            Nota 3: {i["Nota3"]}
            Nota 4: {i["Nota4"]}
            """)
    #Deletar
    elif acao == 3:
        while True:
            achou = False
            delete = str(input("Digite o nome do Aluno que deseja Deletar: "))  
            for i in bd:
                if i["nome"] == delete:
                    ind = bd.index(i)
                    print(ind)
                    bd.pop(ind)
                    achou = True
                    break
            if achou == True:
                break

    #Erro
    else:
        print("Inválido!")
        continue