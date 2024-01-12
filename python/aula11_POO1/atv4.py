#Incompleto
class Calculadora:
    def __init__(self, n1:float, n2:float):
        self.n1 = n1
        self.n2 = n2

    def somar(self):
        soma = self.n1+self.n2
        return soma

    def subtrair(self):
        subtracao = self.n1-self.n2
        return subtracao

    def multiplicar(self):
        multiplicacao = self.n1*self.n2
        return multiplicacao

    def dividir(self):
        
        divisao = self.n1/self.n2
        return divisao
    
while True:
    number1 = float(input("Digite um número: "))
    operacao = str(input("Operação ('+' '-' '*' '/'): "))
    number2 = float(input("Digite outro número: "))
    math = Calculadora(n1=number1, n2=number2)
    print(math.somar())