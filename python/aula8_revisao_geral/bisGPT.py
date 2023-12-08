# FAÇA UM PROGRAMA DE SORTEIO DE CLIENTES ONDE O PROGRAMA VAI CADASTRANDO CLIENTES ATÉ O PROPRIO USUÁRIO DECIDIR QUE QUER PARAR(LOOP INFINITO)
# OS DADOS PARA CADASTRO SÃO: nome, cpf, valor_compra
# QUANDO O USUÁRIO ENCERRAR O LOOP FAÇA UM SORTEIO ENTRE TODOS OS CLIENTES CADASTRADOS E MOSTRE NA TELA TODOS OS DADOS DO CLIENTE QUE FOI SELECIONADO COM UMA MENSAGEM CUSTOMIZADA TIPO:
# """Parabéns {nome do cliente}, cpf: {cpf do cliente} você foi o sorteado por ter feito uma compra no valor de {valor da compra do cliente}"""

import random
import verifica

clientes = []

print("Se você desejar sair digite 'sair' no campo 'nome'")

while True:
    while True:
        nome = str(input("Digite o nome: ")).upper().strip()
        teste1 = verifica.v_nome(nome)
        if teste1 == True:
            break
    if nome == "SAIR":
        break
    while True:
        cpf = int(input("Digite o CPF (apenas números): "))
        teste2 = verifica.v_cpf(cpf)
        if teste2 == True:
            break
    while True:
        valor = float(input("Digite o valor da compra: "))
        teste3 = verifica.v_valor(valor)
        if teste3 == True:
            break

    candidato = {
        "nome" : nome,
        "cpf" : cpf,
        "valor" : valor
    }
    clientes.append(candidato)
    print("Cliente Registrado!")

campeão = random.choice(clientes)

print(f"""Parabéns {campeão["nome"]}, cpf: {campeão["cpf"]} você foi o sorteado por ter feito uma compra no valor de {campeão["valor"]}""")