def contadora(caracters):
    contador_de_letra = 0
    contador_de_espacos = 0
    contador_de_pontuacao = 0
    if " " in caracters:
        for letra in caracters:
            if letra == " ":
                contador_de_espacos += 1
            elif letra.lower() in "abcdefgijklmnopqrstuvxywzáéíóúéêãê":
                contador_de_letra += 1
            elif letra in ".,;?!:":
                contador_de_pontuacao += 1
        return {
            "letras": contador_de_letra,
            "espacos": contador_de_espacos,
            "pontuacao": contador_de_pontuacao
        }
    else:
        return len(caracters)



texto = str(input("Digite um texto ou uma palavra: ")).strip()
resposta = contadora(texto)

print(f"""
    A frase digitado contém:
    Quantidade de letras:{resposta["letras"]}
    Quantidade de espaços:{resposta["espacos"]}
    Quantidade de pontuação:{resposta["pontuacao"]}
""")