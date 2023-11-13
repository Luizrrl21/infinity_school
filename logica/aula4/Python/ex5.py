#Altere o programa anterior permitindo ao usuário informar as populações e as taxas
#de crescimento iniciais. Valide a entrada e permita repetir a operação.

while True:
    a_qtd = int(input("Digite a quantidade de habitantes da população A: "))
    a_tx = float(input("Digite a taxa (%) de crescimento da população A: "))/100
    b_qtd = int(input("Digite a quantidade de habitantes da população B: "))
    b_tx = float(input("Digite a taxa (%) de crescimento da população B: "))/100

    
    ano = 0

    while True:
        ano = ano + 1
        a_qtd = int((a_qtd * a_tx) + a_qtd)
        b_qtd = int((b_qtd * b_tx) + b_qtd)
        if a_qtd >= b_qtd:
            break

    print(f"Levaram {ano} anos para a população A ({a_qtd} habitantes) superar ou igualar a população B ({b_qtd} habitantes)")
    continuar = str(input("Deseja repetir o teste? (Digite 's' para sim ou 'n' para não)"))
    if continuar == 'n':
        break
    elif continuar != 's':
        print("Resposta não entendida, tente novamente!")
        continuar = str(input("Deseja repetir o teste? (Digite 's' para sim ou 'n' para não): "))
    