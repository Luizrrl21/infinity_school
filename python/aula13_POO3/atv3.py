class Aluno:
    def __init__(self, nome:str, idade:int, matricula:str):
        self.__nome = nome
        self.__idade = idade
        self.__matricula = matricula

    def getNome(self):
        return self.__nome
    
    def setNome(self, novo_valor):
        self.__nome = novo_valor
        return self.__nome
    
    def getIdade(self):
        return self.__idade
    
    def setIdade(self, novo_valor):
        self.__idade = novo_valor
        return self.__idade
    
    def getMatricula(self):
        return self.__matricula
    
    def setMatricula(self, novo_valor):
        self.__matricula = novo_valor
        return self.__matricula

aluno1 = Aluno(nome="Luiz", idade=21, matricula="A1B2C3")

print(f"""
      Aluno: {Aluno.getNome(aluno1)}
      Idade: {Aluno.getIdade(aluno1)}
      Matricula: {Aluno.getMatricula(aluno1)}
""")

print("-----------------------------------------------")

print(f"""
      Aluno: {Aluno.setNome(aluno1, "Roberto")}
      Idade: {Aluno.setIdade(aluno1, 22)}
      Matricula: {Aluno.setMatricula(aluno1, "E4F5G6")}
""")
