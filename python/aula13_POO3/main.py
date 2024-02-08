class Autor:
    def __init__(self, nome:str, idade:int, nacionalidade:str):
        self.nome = nome
        self.idade = idade
        self.nacionalidade = nacionalidade

class Livro:
    def __init__(self, titulo:str, autor:object, genero:str, qtde_paginas:int):
        self.titulo = titulo
        self.autor = autor
        self.genero = genero
        self.qtde_paginas = qtde_paginas

autor1 = Autor(nome="Joãozim", idade=52, nacionalidade="Brasileiro")
livro1 = Livro(titulo="Histórias do joão", autor=autor1, genero="Drama", qtde_paginas=1)

print(livro1.titulo)
print(livro1.autor.nacionalidade)