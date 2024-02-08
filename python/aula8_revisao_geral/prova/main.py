from funcoes import *

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

        match menu:
            case 1:
                add(bd)
            case 2:
                if bd == []:
                    print("Vázio, tente adicionar um item primeiro")
                else:
                    ver(bd)
            case 3:
                if bd == []:
                    print("Vázio, tente adicionar um item primeiro")
                else:
                    att(bd)
            case 4:
                if bd == []:
                    print("Vázio, tente adicionar um item primeiro")
                else:
                    rem(bd)
            case 0:
                print(f"{cores(texto='Compra finalizada, total a pagar:', cor='green')} R${totalProdutos}")
                break
            case _:
                print(cores("ERRO! Número Inválido!","red"))
                continue
        
        totalProdutos = total(bd)
        print(f'{cores(f"Valor Total: ","blue")} R${total(bd)}')
    except:
        print(cores("ERRO! Digite um número do menu","red"))