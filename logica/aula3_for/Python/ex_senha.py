#FAÇA UM PROGRAMA QUE PEDE PRO USUÁRIO DIGITAR UMA SENHA E VERIFICA SE ESSA SENHA É FORTE
#REQUISITOS PARA UMA SENHA FORTE:

#POSSUI NÚMEROS, LETRAS MÁIUSCULAS, MNÚSCULAS E CARACTER ESPECIAL

numeros = "123456789"
maiuscula = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
minuscula = "abcdefghijklmnopqrstuvwxyz"
caracter = "!@#$%¨&*()-_=+/?°₢,.<>;:/?]}~^ç[''""]"

senha = str(input("Crie sua senha: "))

for i in senha:
    print(i)