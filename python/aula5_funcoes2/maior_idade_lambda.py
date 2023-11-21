idade = int(input("Digite a idade: "))

verifica = lambda idade : "Maior de idade" if idade > 18 else "Menor de idade"

print(verifica(idade))