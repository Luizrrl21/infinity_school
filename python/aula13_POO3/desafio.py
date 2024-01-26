class Livro:
    def __init__(self, titulo:str, autor:str):
        self.__titulo = titulo
        self.__autor = autor

    def getTitulo(self):
        return self.__titulo
    
    def getAutor(self):
        return self.__autor
    
class Usuario:
    def __init__(self, id:str, nome:str):
        self.__id = id
        self.__nome = nome

    def getId(self):
        return self.__id
    
    def setId(self, novoId:str):
        self.__id = novoId
        return self.__id
    
    def getNome(self):
        return self.__nome
    
    def setNome(self, novoNome:str):
        self.__nome = novoNome
        return self.__id
    
class Biblioteca:
    def __init__(self, livros:list):
        pass