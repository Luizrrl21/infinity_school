class Moto:
    def __init__(self, marca=str, modelo=str, cilindradas=int, cor=str):
        self.marca = marca
        self.modelo = modelo
        self.cilindradas = cilindradas
        self.cor = cor

    def ligar(self):
        return f"A {self.modelo} ligou"
    
    def ver_informacoes(self):
        return f"""
        Marca: {self.marca}
        Modelo: {self.modelo}
        Cilindradas: {self.cilindradas}
        Cor: {self.cor}               
    """

moto1 = Moto(marca= "Harley-Davidson", modelo="883 Iron", cilindradas=883,  cor="Preto")
moto2 = Moto(marca= "Harley-Davidson", modelo="Fat Boy", cilindradas=1584,  cor="Branca")
moto3 = Moto(marca= "Harley-Davidson", modelo="V-ROD Muscle", cilindradas=1247,  cor="preto")

print(moto1.ligar())
print(moto2.ligar())
print(moto3.ligar())