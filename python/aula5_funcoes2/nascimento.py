import datetime

ano = int(input("Ano de nascimento: "))
atual = datetime.date.today().year

verifica = lambda ano : "Maior de idade" if (atual-ano) > 18 else "Menor de idade"

print(verifica(ano))