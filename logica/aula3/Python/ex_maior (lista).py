#FAÇA UM PROGRAMA QUE PEDE PRO USUÁRIO INSERIR 5 NÚMEROS E EXIBA NA TELA QUAL FOI O MAIOR DOS 5

numeros = []

for i in range(5):
    numero = int(input("Digite um número: "))
    numeros.append(numero)

print(max(numeros))
 