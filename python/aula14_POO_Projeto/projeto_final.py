contador_id_livro = 1
contador_id_membro = 1

class Livro:
    def __init__(self, titulo:str, autor:str, id:int):
        self.titulo = titulo
        self.autor = autor
        self.id = id
        self.disponivel = True

class Membro:
    def __init__(self, nome:str, id:int):
        self.nome = nome
        self.id = id
        self.historico = []

class Biblioteca:
    def __init__(self):
        self.catalogo = []
        self.membros = []

    def adicionar_membros(self):
        global contador_id_membro
        nome = str(input("Nome do Membro: "))
        membro = Membro(nome=nome, id=contador_id_membro)
        contador_id_membro += 1
        self.membros.append(membro)
    
    def adicionar_livros(self):
        global contador_id_livro
        titulo = str(input("Título do Livro: "))
        autor = str(input("Autor do Livro: "))
        livro = Livro(titulo=titulo, autor=autor, id=contador_id_livro)
        contador_id_livro += 1
        self.catalogo.append(livro)
    
    def pesquisa_livro(self):
        escolha = str(input("Digite o ID ou Título do livro que você deseja: "))
        for livro_atual in self.catalogo:
            if livro_atual.titulo == escolha or livro_atual.id == int(escolha):
                print(f"""
                        Informações do livro pesquisado:
                        Título do Livro: {livro_atual.titulo}
                        ID do livro: {livro_atual.id}
                        Autor do Livro: {livro_atual.autor}
                        Disponibilidade do livro: {livro_atual.disponivel}
                        """)

    def emprestimo(self):
        id_membro = int(input("Digite o ID do membro que vai pegar o livro emprestado: "))
        for membro_atual in self.registro_membros:
            if membro_atual.id == id_membro:
                id_livro = int(input(f"{membro_atual.nome} escolha o ID do livro que você quer emprestado: "))
                for livro_atual in self.catalogo_livros:
                    if livro_atual.id == id_livro:
                        if livro_atual.status_disponivel:
                            livro_atual.status_disponivel = False
                            membro_atual.historico.append(livro_atual)
                            return "Livro emprestado com sucesso"
                        else:
                            return "Livro encontrado porém já está emprestado"
                    else:
                        return "Livro não encontrado"
            else:
                return "Membro não encontrado" 
    
    def devolucao(self):
        id_livro = int(input("Escolha o ID do livro que você quer devolver: "))
        for livro_atual in self.catalogo_livros:
            if livro_atual == id_livro:
                if livro_atual.status_disponivel:
                    livro_atual.status_disponivel = True
                    return "Livro devolvido com sucesso"
                else:
                    return "Livro encontrado porém já está disponível"
            else:
                return "Livro não encontrado"

biblioteca = Biblioteca()

while True:
    try:
        acao = int(input("""
        Escolha uma opção:
        1 - Adicionar Livro
        2 - Adicionar Membro
        3 - Pesquisar Livro
        4 - Emprestar Livro
        5 - Devolver Livro
        0 - Sair
    """))

        match acao:
            case 0:
                print("SISTEMA FECHADO")
                break

            case 1:
                biblioteca.adicionar_livros()

            case 2:
                biblioteca.adicionar_membros()

            case 3:
                biblioteca.pesquisa_livro()

            case 4:
                biblioteca.emprestimo()

            case 5:
                biblioteca.devolucao()

            case _:
                print("ERRO! Digite um número de 0 a 5")

    except:
        print("ERRO! Digite um número de 0 a 5")