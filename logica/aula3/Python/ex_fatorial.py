n = int(input("Digite um valor: "))
fatorial = 1

for i in range(n,1,-1):
    fatorial = fatorial * i

print(f"O fatorial de {n} é {fatorial}")
