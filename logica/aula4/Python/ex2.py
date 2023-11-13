while True:
    user = str(input("Digite seu nome de usuário: "))
    senha = str(input("Digite sua senha: "))
    if user == senha:
        print("O nome de usuário deve ser diferente da senha! Tente Novamente")
    else:
        print("Usuário criado, bem vindo!")
        break