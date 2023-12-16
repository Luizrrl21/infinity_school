def transformar_maiusculo(texto):
    return texto.upper()

def transformar_minusculo(texto):
    return texto.lower()

def contar_vogais(texto):
    contador = 0
    for letra in texto:
        if letra.lower()  in "aeiou":
            contador += 1
    return contador

def contar_consoantes(texto):
    contador = 0
    for letra in texto:
        if letra.lower()  in "bcdfghjklmnpqrstvwxyz":
            contador += 1
    return contador