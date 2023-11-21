import os
from jokenpo import cond_jokenpo
from jokenpo import opcoes

while True:
    pontos_user = 0
    pontos_bot = 0
    escolha = str(input("Escolha uma opção: ")).lower()

    if escolha == "sair":
        print("Obrigado por jogar!")
        print("---------------------------------")
        print(f"Meu total: {pontos_user} pontos")
        print(f"Máquina: {pontos_bot} pontos")
        break
    
    elif escolha in opcoes:
        os.system('cls')
        dicionario = cond_jokenpo(escolha=escolha)
        pontos_bot = pontos_bot + int(dicionario['bot'])
        pontos_user = pontos_user + int(dicionario['user'])

    else:
        print("Erro, tente novamente!")