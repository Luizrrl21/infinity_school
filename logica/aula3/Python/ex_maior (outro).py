#FAÇA UM PROGRAMA QUE PEDE PRO USUÁRIO INSERIR 5 NÚMEROS E EXIBA NA TELA QUAL FOI O MAIOR DOS 5

maior_numero = 0

for i in range(5):
    numero = int(input("Digite um número: "))
    if numero > maior_numero:
        maior_numero = numero

print(f"O maior número é {maior_numero}")

