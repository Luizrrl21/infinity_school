class Carro:
    def __init__(self, marca:str, cor:str, modelo:str, ano:int, qtde_portas:int):
        self.marca = marca
        self.cor = cor
        self.modelo = modelo
        self.ano = ano
        self.qtde_portas = qtde_portas

carro1 = Carro(marca="Gol", cor="preto", modelo="teste", ano=2023, qtde_portas=4)

print(carro1.marca)