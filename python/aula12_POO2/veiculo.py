class Veiculo:
    def __init__(self, marca:str, modelo:str, ano:int, cor:str):
        self.marca = marca
        self.modelo = modelo
        self.ano = ano
        self.cor = cor
    def ligar(self):
        return f"O veículo {self.modelo} ligou"

class Carro(Veiculo):
    def __init__(self, marca: str, modelo: str, ano: int, cor: str, qtde_portas:int):
        super().__init__(marca, modelo, ano, cor)
        self.qtde_portas = qtde_portas

    def cavalo_de_pau(self):
        return f"O carro {self.modelo} que tem {self.qtde_portas} de portas fez um cavalo de pau"

class Moto(Veiculo):
    def __init__(self, marca: str, modelo: str, ano: int, cor: str, cilindradas: int):
        super().__init__(marca, modelo, ano, cor)
        self.cilindradas = cilindradas
    def empinar(self):
        return f"A moto {self.modelo} de {self.cilindradas} cilindradas está empinando"
    
carro1 = Carro(marca="Fiat", modelo="Uno", ano=2004, cor="Azul escuro", qtde_portas=2)
moto1 = Moto(marca="Honda", modelo="XRE", ano=2020, cor="Vermelho", cilindradas=300)

