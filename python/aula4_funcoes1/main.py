def saudacao(nome):
    print(f"Olá {nome}, seja bem vindo")

for i in range(10):
    nome = str(input("Digite seu nome: "))
    saudacao(nome)