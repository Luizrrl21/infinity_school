class Veiculo:
    def __init__(self, cor:str, marca:str, modelo:str):
        self.cor = cor
        self.cor = marca

class Carro(Veiculo):
    def __init__(self, cor: str, marca: str):
        super().__init__(cor, marca)

class Bicicle(Veiculo):
    def __init__(self, cor: str, marca: str):
        super().__init__(cor, marca)