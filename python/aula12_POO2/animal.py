class Animal:
    def __init__(self, nome:str, raca:str, idade:int, cor:str):
        self.nome = nome
        self.raca = raca
        self.idade = idade
        self.cor = cor

    def emitir_som(self):
        return "Som indefinido"
    
class Gato(Animal):
    def __init__(self, nome: str, raca: str, idade: int, cor: str):
        super().__init__(nome, raca, idade, cor)
    def emitir_som(self):
        return "Miauuuu"
    
class Cachorro(Animal):
    def __init__(self, nome: str, raca: str, idade: int, cor: str):
        super().__init__(nome, raca, idade, cor)
    def emitir_som(self):
        return "Au au"
    
gatim = Gato(nome="Xaninho", raca="Dos preto", idade=6, cor="Branco")
cachorrim = Cachorro(nome="Iscubidu", raca="Vira-Lata", idade=4, cor="Caramelo")
porco = Animal(nome="Bacon", raca="Dos fofim", idade=1, cor="Rosa")