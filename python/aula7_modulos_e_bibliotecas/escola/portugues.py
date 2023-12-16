def palindromo(texto:str):
    return texto[::-1]

def contar_caract(texto:str):
    return len(texto)

def contar_v_e_c(texto):
    cont_vogal = 0
    cont_conso = 0
    for letra in texto:
        if letra.lower() in "aeiou":
            cont_vogal += 1
        elif letra.lower() in "bcdfghjklmnpqrstvwxyz":
            cont_conso += 1
    return [cont_vogal, cont_conso]

