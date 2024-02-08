from funcoes import *
import os

bd = []

while True:
    try:
        menu = int(input(cores(texto=f"""
        
        **************************
        Escolha uma opção no menu:
                            
        1 - Adicionar Produto
        2 - Ver a lista de Produtos
        3 - Atualizar Produtos
        4 - Remover Produto
        0 - Finalizar Compra
                               
        **************************
                            
        Opção: """, cor="yellow")))
        
        print("")

        os.system("cls")
        match menu:
            case 1:
                add(bd)
            case 2:
                if bd == []:
                    print("Vázio, tente adicionar um valor primeiro")
                else:
                    ver(bd)
            case 3:
                print("Att")
            case 4:
                print("Del")
            case 0:
                break
            case _:
                print(cores("ERRO! Número Inválido!","red"))
                continue
        
        totalProdutos = total(bd)
        print(f'{cores(f"Valor Total: ","blue")} R${total(bd)}')
    except:
        os.system("cls")
        print(cores("ERRO! Digite um número do menu","red"))