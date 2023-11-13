x = str(input("Digite uma palavra: "))
vogais = "AEIOUaeiou"
soma = 0

for i in x:
    if i in vogais:
        soma = soma + 1

print(f"A palavra {x} tem {soma} vogais!")