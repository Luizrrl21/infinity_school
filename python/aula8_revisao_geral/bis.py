# FAÇA UM PROGRAMA DE SORTEIO DE CLIENTES ONDE O PROGRAMA VAI CADASTRANDO CLIENTES ATÉ O PROPRIO USUÁRIO DECIDIR QUE QUER PARAR(LOOP INFINITO)
# OS DADOS PARA CADASTRO SÃO: nome, cpf, valor_compra
# QUANDO O USUÁRIO ENCERRAR O LOOP FAÇA UM SORTEIO ENTRE TODOS OS CLIENTES CADASTRADOS E MOSTRE NA TELA TODOS OS DADOS DO CLIENTE QUE FOI SELECIONADO COM UMA MENSAGEM CUSTOMIZADA TIPO:
# """Parabéns {nome do cliente}, cpf: {cpf do cliente} você foi o sorteado por ter feito uma compra no valor de {valor da compra do cliente}"""

import random

clientes = []

print("Se você desejar sair digite 'sair' no campo 'nome'")

while True:
    try:
        while True:
            nome = str(input("Digite o nome: ")).upper()
            for i in nome:
                if nome in "qwertyuiopasdfghjklçzxcvbnm":
                    break
        if nome == "SAIR":
            break
        cpf = int(input("Digite o CPF (apenas números): "))
        valor = float(input("Digite o valor da compra: "))

        candidato = {
            "nome" : nome,
            "cpf" : cpf,
            "valor" : valor
        }
        clientes.append(candidato)
        print("Cliente Registrado!")

    except:
        print("Você preencheu um tipo de dado errado, tente novamente!")
        print("OBS: Digite apenas números no CPF e no Valor")
        continue           


campeão = random.choice(clientes)

print(f"""Parabéns {campeão["nome"]}, cpf: {campeão["cpf"]} você foi o sorteado por ter feito uma compra no valor de {campeão["valor"]}""")