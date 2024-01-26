class Conta:
    def __init__(self, numero:int,titular:str,saldo:float):
       self.numero = numero
       self.titular = titular
       self.saldo = saldo

    def depositar(self, valor):
        self.saldo += valor
        return self.saldo

    def sacar(self, valor):
        if self.saldo >= valor:
            self.saldo -= valor
            return self.saldo
        else:
            print("Saldo insuficiente")

    def ver_saldo(self):
        return self.saldo

    def resumo(self):
        return f"""
    Informações da conta:
    Número da conta: {self.numero}
    Titular da conta: {self.titular}
    Saldo da conta: {self.saldo}
"""


class ContaCorrente(Conta):
    def __init__(self, numero: int, titular: str, saldo: float, taxa_manutencao:float, limite_cheque:float):
        super().__init__(numero, titular, saldo)
        self.taxa_manutencao = taxa_manutencao
        self.limite_cheque = limite_cheque
    
    def sacar(self, valor):
            if self.saldo + self.limite_cheque >= valor:
                self.saldo = self.saldo - valor
                return self.saldo
            else:
                print("Saldo insuficiente")

class ContaPoupanca(Conta):
    def __init__(self, numero: int, titular: str, saldo: float, taxa_juros:float):
        super().__init__(numero, titular, saldo)
        self.taxa_juros = taxa_juros

    def calcular_juros(self):
        valor_adicional = self.saldo * self.taxa_juros
        self.saldo += valor_adicional