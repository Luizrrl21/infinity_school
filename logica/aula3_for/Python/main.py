alfabeto = "abcdefghijklmnopqrstuvwxyz"
vogais = "aeiou"

for letra in alfabeto:
    if letra not in vogais:
        print(f"{letra} é uma consoante")