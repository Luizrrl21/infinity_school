numero = int(input("Digite um valor: "))
condicao = True

for i in range(2,numero):
    div1 = numero / i
    div2 = numero // i
    if div1 == div2:
        condicao = False

if numero < 2:
    print(f"O número {numero} não é Primo!")
elif condicao == True:
    print(f"O número {numero} é Primo!")
else:
    print(f"O número {numero} não é Primo!")


