#Classe
class Elevador:
    def __init__(self, totalCapacidade:int, atualCapacidade:int, totalAndar:int, atualAndar:int):
        self.totalCapacidade = totalCapacidade
        self.atualCapacidade = atualCapacidade
        self.totalAndar = totalAndar
        self.atualAndar = atualAndar

    def Subir(self):
        if self.atualAndar == self.totalAndar:
            print("VOCÊ ESTÁ NO ANDAR MAIS ALTO!")
        else:
            self.atualAndar += 1
            print(f"Subindo. {self.atualAndar}º andar")

    def Descer(self):
        if self.atualAndar < 1:
            print("VOCÊ JÁ ESTÁ NO TÉRREO!")
        else:
            self.atualAndar -= 1
            print(f"Descendo. {self.atualAndar}º andar")

    def Entrar(self):
        if self.atualCapacidade == self.totalCapacidade:
            print("O ELEVADOR ESTÁ CHEIO!")
        else:
            self.atualCapacidade = self.atualCapacidade + 1
            print(f"Entrando uma pessoa. {self.atualCapacidade} pessoas")

    def Sair(self):
        if self.atualCapacidade < 1:
            print("NÃO TEM NINGUÉM")
        else:
            self.atualCapacidade -= 1
            print(f"Saindo uma pessoa. {self.atualCapacidade} pessoas")

#Teste instanciamento
elevador1 = Elevador(totalCapacidade = 8, atualCapacidade = 0, totalAndar = 15, atualAndar = 0)
while True:
    try:
        acao = int(input("""
                     1 - Subir
                     2 - Descer
                     3 - Entrar
                     4 - Sair
                     0 - Parar

                     Ação Elevador: """))
    
        match acao:
            case 1:
                elevador1.Subir()
            case 2:
                elevador1.Descer()
            case 3:
                elevador1.Entrar()
            case 4:
                elevador1.Sair()
            case 0:
                break
            case _:
                print("Opção inválida (De 0 a 4)")
    except:
        print("Opção Inválida (Apenas Número)")

