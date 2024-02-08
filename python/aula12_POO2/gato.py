class Gato:
    def __init__(self, nome:str, raca:str, peso:float, idade:int, castrado:bool):
        self.nome = nome
        self.raca = raca
        self.peso = peso
        self.idade = idade
        self.castrado = castrado

    def miar(self):
        return f"O {self.nome} está miando, dê atenção pra ele"

gato1 = Gato("Tafarel", "Persa", 1.5, 2, True)
gato2 = Gato("Xanin", "Bombay", 0.8, 1, False)
print(gato1.miar())
print(gato2.miar())