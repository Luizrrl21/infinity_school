from datetime import datetime

class Funcionario:
    def __init__(self, nome:str, cpf:str, idade:int):
        self.nome = nome
        self.cpf = cpf
        self.idade = idade

    def bater_ponto(self):
        horario = datetime.now().strftime("%H:%M")
        return f"{self.nome} bateu ponto as {horario}h"
    
class Gerente(Funcionario):
    def __init__(self, nome: str, cpf: str, idade: int):
        super().__init__(nome, cpf, idade)
    
    def contratar(self):
        return f"O gerente {self.nome} contratou alguem"
    
    def demitir(self):
        return f"O gerente {self.nome} demitiu alguem"

class Caixa(Funcionario):
    def __init__(self, nome: str, cpf: str, idade: int, num_caixa:int):
        super().__init__(nome, cpf, idade)
        self.num_caixa = num_caixa

    def fechar_caixa(self):
        return f"O {self.nome} fechou o caixa {self.num_caixa}"
    
gerente = Gerente(nome="Luiz", cpf="123.456.789-10", idade=21)
caixa = Caixa(nome="Niuzilene", cpf= "109.876.543-21", idade= 22, num_caixa=1)

print(gerente.contratar())
print(gerente.demitir())
print(gerente.contratar())

print(caixa.fechar_caixa())
print(caixa.bater_ponto())