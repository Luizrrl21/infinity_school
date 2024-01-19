class Conta:
    def __init__(self, num_conta:int, titular:str, saldo:float):
        self.num_conta = num_conta
        self.titular = titular
        self.saldo = saldo

    def depositar(self):
        valor = float(input("Valor do Depósito: R$"))
        self.saldo = valor + self.saldo
        print(f"Saldo atual: R${self.saldo}")
        return self.saldo
    
    def sacar(self):
        valor = float(input("Valor do Saque: R$"))
        if valor > self.saldo:
            print("Saldo Insuficiente!")
        else:
            self.saldo = self.saldo - valor
        print(f"Saldo atual: R${self.saldo}")
        return self.saldo
    
    def verSaldo(self):
        print(f"Saldo atual: R${self.saldo}")
        return self.saldo

class ContaCorrente(Conta):
    def __init__(self, num_conta: int, titular: str, saldo: float, taxa_manutencao:float, limite_cheque: float):
        super().__init__(num_conta, titular, saldo)
        self.taxa_manutencao = taxa_manutencao
        self.limite_cheque = limite_cheque

    def sacar(self):
        valor = float(input("Valor do Saque: R$"))
        if valor > self.saldo and valor < self.limite_cheque:
            while True:
                cheque = str(input(f"Saldo Insuficiente! Deseja usar Cheque Especial? (Limite R${self.limite_cheque}) (Y/n)"))
                if cheque == "n":
                    break
                elif cheque == "Y":
                    self.limite_cheque = self.limite_cheque - valor
                    print(f"Saldo atual: R${self.saldo}")
                    print(f"Limite Cheque: R${self.limite_cheque}")
                    break
                else:
                    print("Erro! Digite apenas 'Y' para sim ou 'n' para não")
        else:
            self.saldo = self.saldo - valor
            print(f"Saldo atual: R${self.saldo}")
        return self.saldo


user = ContaCorrente(num_conta=123, titular="Luiz Roberto", saldo=0.0, taxa_manutencao=0.5, limite_cheque=1000)
user.verSaldo()
