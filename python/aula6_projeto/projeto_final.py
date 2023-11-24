import random

opcoes = ["pedra", "papel", "tesoura"]

def view(texto1: str, texto2: str):
    print("")
    print("**************************************")
    print(texto1)
    print(texto2)
    print("**************************************")
    print("")

def bot_jokenpo():
    return random.choice(opcoes)

def cond_jokenpo(escolha: str, maquina: str = bot_jokenpo()):
    #Empate
    if escolha == maquina:
        view(f"Você: {escolha} x Máquina: {maquina}","\033[0;49;33m Empate! \033[0;0m")

        return {
            "user" : 0,
            "bot" : 0
        }
    
    #Vitória
    elif (escolha == "papel" and maquina == "pedra") or (escolha == "pedra" and maquina == "tesoura") or (escolha == "tesoura" and maquina == "papel"):
        view(f"Você: {escolha} x Máquina: {maquina}","\033[0;49;32m Você ganhou! \033[0;0m")

        return {
            "user" : 1,
            "bot" : 0
        }
    
    #Derrota
    else:
        view(f"Você: {escolha} x Máquina: {maquina}", "\033[0;49;31m Você perdeu! \033[0;0m")

        return {
            "user" : 0,
            "bot" : 1
        }

pontos_user = 0
pontos_bot = 0

print("\033[7;49;36m O JOGO COMEÇOU! \033[0;0m")
print("---------------------------------")

while True:
    escolha = str(input("\033[0;49;36m Escolha uma opção: \033[0;0m")).lower()
    if escolha not in opcoes:
        print(f"\033[0;49;36m Opção inválida! Tente: {opcoes}\033[0;0m")
        continue
    dicionario = cond_jokenpo(escolha=escolha, maquina = bot_jokenpo())
    
    pontos_user += int(dicionario['user'])
    pontos_bot += int(dicionario['bot'])

    while True:
        acao = str(input("\033[0;49;36m Deseja jogar de novo? \033[0;0m")).lower()
        if acao == "sim" or acao == "nao" or acao == "não":
            break
        else:
            print("\033[0;49;31m Sim ou Não?\033[0;0m")
    
    if acao == "nao" or acao == "não":
        break

if pontos_user > pontos_bot:
    view("\033[0;49;32m PARABÉS! :) Placar final:\033[0;0m", f"Você: {pontos_user} x Bot: {pontos_bot}")

else:
    view("\033[0;49;31m MELHORE! :( Placar final:\033[0;0m", f"Você: {pontos_user} x Bot: {pontos_bot}")