import os

os.system('cls')
while True:
    senha = str(input("Digite sua senha: "))
    if len(senha) >= 8 and len(senha) <= 12:
        os.system('cls')
        print("Senha validada!")
        break
    else:
        os.system('cls')
        print("A senha não atende aos critérios (mín 8 e máx 12 letras), tente novamente!")