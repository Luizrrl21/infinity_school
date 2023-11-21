opcoes = ["pedra", "papel", "tesoura"]

def bot_jokenpo():
    import random
    return random.choice(opcoes)

def cond_jokenpo(escolha: str, maquina: str = bot_jokenpo()):
    #Erro
    if escolha not in opcoes:
        print(f"Escolha uma opção válida: {opcoes}")
    #Empate
    elif escolha == maquina:
        print(f"Você: {escolha} x Máquina: {maquina}")
        print("Empate!")
        print("**************************************")
        return {
            "condicao" : "empate",
            "user" : 0,
            "bot" : 0
        }
    #Vitória
    elif (escolha == "papel" and maquina == "pedra") or (escolha == "pedra" and maquina == "tesoura") or (escolha == "tesoura" and maquina == "papel"):
        print(f"Você: {escolha} x Máquina: {maquina}")
        print(f"Você ganhou!")
        print("**************************************")
        return {
            "condicao" : "vitória",
            "user" : 1,
            "bot" : 0
        }
    #Derrota
    else:
        print(f"Você: {escolha} x Máquina: {maquina}")
        print(f"Você perdeu!")
        print("**************************************")
        return {
            "condicao" : "derrota",
            "user" : 0,
            "bot" : 1
        }