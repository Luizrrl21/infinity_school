letra = str(input("Digite uma letra: "))
vogais = {"a","A","e","E","i","I","o","O","u","U"}

if letra in vogais:
    print(f"A letra '{letra}' é uma vogal")
else:
    print(f"A letra '{letra}' é uma consoante")
