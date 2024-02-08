# Crie instâncias das classes "Livro" e "Revista" com informações específicas e chame o método "exibir_informacoes" para mostrar os detalhes de cada material.

#Classes
class Material:
    def __init__(self, titulo:str, autor_ou_editora:str):
        self.titulo = titulo
        self.autor_ou_editora = autor_ou_editora

    def exibir_informacoes(self):
        return {"título":self.titulo, "autor/editora":self.autor_ou_editora}
    
class Livro(Material):
    def __init__(self, titulo:str, autor_ou_editora:str, genero:str):
        super().__init__(titulo, autor_ou_editora)
        self.genero = genero

    def exibir_informacoes(self):
        return {"título":self.titulo, "autor/editora":self.autor_ou_editora, "genero":self.genero}
    
class Revista(Material):
    def __init__(self, titulo: str, autor_ou_editora: str, edicao:str):
        super().__init__(titulo, autor_ou_editora)
        self.edicao = edicao

    def exibir_informacoes(self):
        return {"título":self.titulo, "autor/editora":self.autor_ou_editora, "edicao":self.edicao}
    
#Instâncias
book = Livro("Senhor dos anéis", "J. R. R. Tolkien", "Fantasia")
magazine = Revista("Veja", "Editora Abril", "2878 - 02/02/2024")

print(book.exibir_informacoes())
print(magazine.exibir_informacoes())
        