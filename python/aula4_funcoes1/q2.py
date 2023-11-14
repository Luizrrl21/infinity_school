def letras(caracters):
    
    contador_letra = 0
    contador_espaco = 0
    contador_sinal = 0

    if " " in caracters:
        for letra in caracters:
            if letra == " ":
                contador_espaco += 1
            elif letra.lower() in "abcdefghijklmnopqrstuvwxyz":
                contador_letra += 1
            elif letra in ".,;?!:":
                contador_sinal += 1
        return f"A frase tem {contador_letra} caracters, {contador_espaco} espaços e {contador_sinal} sinais"
    else:
        return len(caracters)

texto = str(input("Digite um texto ou uma palavra: ")).strip()

print(letras(texto))