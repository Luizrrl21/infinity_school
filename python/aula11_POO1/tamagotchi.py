class Tamagotchi:
    def __init__(self, nome, especie, energia):
        self.nome = nome
        self.especie = especie
        self.energia = energia

    def brincar(self):
        if self.energia >= 0:
            self.energia = self.energia - 5
        else:
            print("Seu Tamagotvhi está cansado, tente alimenta-lo primeiro")
        return self.energia
    
    def comer(self):
        if self.energia <= 95:
            self.energia = self.energia + 5
        else:
            print("Tá de buxo cheio")
        return self.energia

tamagotchi1 = Tamagotchi(nome="Xingulingu", especie="Aquatica", energia=100)

while True:
    menu = int(input("""
    Escolha uma opção
    1 - Brincar
    2 - Comer
    0 - Sair
"""))
    
    match menu:
        case 1:
            tamagotchi1.brincar()
        case 2:
            tamagotchi1.comer()
        case 0:
            break
        case _: print("Opção Inválida")


    print(f"Energia atual: {tamagotchi1.energia}")