#Senha com maior de 8 Caracteres, pelo menos uma letra e um número

alfabeto = "abcdefghijklmnopqrstuvwxyz"
numero = "1234567890"

while True:
    #Variáveis
    senha = str(input("Digite uma senha: "))
    tem_letra = False
    tem_numero = False

    for letra in senha:
        if letra in alfabeto:
            tem_letra = True
        elif letra in numero:
            tem_numero = True

    if tem_letra == True and tem_numero == True and len(senha) >=8:
        print("Senha válida! Bem Vindo")        
        break
    else:
        print("Senha inválida! Tente novamente")