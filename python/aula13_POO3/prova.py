class bombaCombustível:
    def __init__(self, tipoCombustivel:str, valorLitro:float, quantidadeCombustivel:float):
        self.__tipoCombustivel__ = tipoCombustivel
        self.__valorLitro__ = valorLitro
        self.__quantidadeCombustivel__ = quantidadeCombustivel

    def abastecerPorValor(self, valorAbastecido):
        reducao = valorAbastecido/self.__valorLitro__
        self.__quantidadeCombustivel__ -= reducao

        return f"""\033[0;49;36m
        Abastecido: {round(reducao,2)} Litros
        Valor: R${round(valorAbastecido,2)}

        (Armazenamento Tanque: {round(self.__quantidadeCombustivel__,2)}L)
        \033[0;0m"""

    def abastecerPorLitro(self, qtdAbastecido):
        reducao = qtdAbastecido
        self.__quantidadeCombustivel__ -= reducao

        return f"""\033[0;49;36m
        Abastecido: {round(reducao,2)} Litros
        Valor: R${round(qtdAbastecido*self.__valorLitro__,2)}

        (Armazenamento Tanque: {round(self.__quantidadeCombustivel__,2)}L)
        \033[0;0m"""
    
    def alterarValor(self, novoValor):
        velho = self.__valorLitro__
        self.__valorLitro__ = novoValor
        return f"\033[0;49;32m Valor alterado de R${round(velho,2)} para R${round(self.__valorLitro__,2)}\033[0;0m"
    
    def alterarCombustivel(self, indexCombustivel):
        opcoes = ["Diesel", "Etanol", "Gasolina Comum", "Gasolina Aditivada"]
        self.__tipoCombustivel__ = opcoes[indexCombustivel]
        return f"\033[0;49;32m Combustível alterado para {self.__tipoCombustivel__}\033[0;0m"
    
    def alterarQuantidadeCombustivel(self, novaQuantidade):
        self.__quantidadeCombustivel__ + novaQuantidade
        return f"\033[0;49;32m Armazenamento de combustível aumentado em  {round(novaQuantidade,2)}L (Armazenamento atual: {round(self.__quantidadeCombustivel__,2)}L)\033[0;0m"
    
    def statusBomba(self):
        return f"""
        Combustível: {self.__tipoCombustivel__}
        Valor: R${round(self.__valorLitro__,2)}
        Armazenamento: {round(self.__quantidadeCombustivel__,2)}L
"""
    
def numero(texto:str = ""):
    while True:
        try:
            numero = float(input(f"{texto}"))
            break
        except:
            print('\033[0;49;31m DIGITE UM NÚMERO! \033[0;0m')
            continue
    return numero
#Teste
bomba1 = bombaCombustível("Gasolina Comum", 5, 10000)

while True:
    try:
        acao = int(input("""
                    1 - Ligar a bomba
                    2 - Ajustar preço
                    3 - Alterar tipo Combustível
                    4 - Alterar quantidade Combustível
                    0 - Sair
    """))
    
    except:
        print("\033[0;49;31m ERRO! Tente um número de 0 a 5 \033[0;0m")
        continue

    match acao:
        case 0:
            print("\033[0;49;33mSISTEMA DESLIGADO!\033[0;0m")
            break

        case 1:
            while True:
                try:
                    acao = int(input("""
                                1 - Abastecer por litro
                                2 - Abastecer por valor
                                0 - Voltar Configurações     
                                    """))
                except:
                    print("\033[0;49;31m ERRO! Tente um número de 0 a 2 \033[0;0m")
                    continue

                if acao == 1:
                    litros = numero("Quantos litros para abastecer: ")
                    resposta = bomba1.abastecerPorLitro(qtdAbastecido=litros)
                    print(resposta)

                elif acao == 2:
                    valor = numero("Qual o valor para abastecer: R$")
                    resposta = bomba1.abastecerPorValor(valorAbastecido=valor)
                    print(resposta)

                elif acao == 0:
                    break

                else:
                    print("\033[0;49;31m ERRO! Tente um número de 0 a 2 \033[0;0m")
        
        case 2:
            novoValor = numero("Novo valor bomba: R$")
            ajuste = bomba1.alterarValor(novoValor)
            print(ajuste)

        case 3:
            while True:
                try:
                    alteracao = int(input("""
                    Escolha o combustível da bomba:
                    0 - Diesel
                    1 - Etanol
                    2 - Gasolina Comum
                    3 - Gasolina Aditivada  
                            """))
                    if alteracao >= 0 and alteracao <= 3:
                        combustivel = bomba1.alterarCombustivel(indexCombustivel=alteracao)
                        print(combustivel)
                        break
                    else:
                        print("\033[0;49;31m ERRO! Tente um número de 0 a 3 \033[0;0m")

                except:
                    print("\033[0;49;31m ERRO! Tente um número de 0 a 3 \033[0;0m")
                    continue
        case 4:
            novaQuantidade = numero("Quantidade de litros adicionadas: ")
            armazenamento = bomba1.alterarQuantidadeCombustivel(novaQuantidade=novaQuantidade)
            print(armazenamento)

        case 5:
            print(bomba1.statusBomba())

        case _:
            print("\033[0;49;31m ERRO! Tente um número de 0 a 5 \033[0;0m")