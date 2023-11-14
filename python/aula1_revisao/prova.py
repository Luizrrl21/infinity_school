import os

email = "teste@gmail.com"
senha = "infinity2023"

os.system('cls')

while True:
    e_input = str(input("Endereço de email: "))
    s_input = str(input("Senha: "))
    os.system('cls')
    if e_input == email and s_input == senha:
        print("Bem vindo!")
        break
    else:
        print("Usuário ou senha estão incorretos! Tente novamente!")