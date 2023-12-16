#[PY-A04] Desenvolva um programa em Python que permita ao usuário digitar várias notas.
#Em seguida, crie uma função chamada "calcular_media" que irá receber as notas digitadas e calcular a média do aluno. 
#Também crie uma função chamada "verificar_situacao" que, com base na média calculada, irá exibir a situação do aluno:
#"Reprovado" se a média for menor que 7, "Aprovado" se a média for maior ou igual a 7, e
#"Parabéns, sua média é 10" se a média for igual a 10.

def media(lista: list):
    return round(sum(lista)/len(lista),2)

def situacao(valor: float):
    if valor == 10:
        return "Parabéns"
    elif valor >= 7:
        return "Aprovado"
    else:
        return "Reprovado"
    
def opcao(choice: str, dados: list, nome:str):
    opcoes = ("add", "sair")
    if choice == "sair":
        return ["sair", f"O aluno {nome} está com a média {media(dados)}. Situação: {situacao(media(dados))}"]
    elif choice == "add":
        while True:
            try:
                nota = float(input("Digite a nota do Aluno: "))
                if nota >= 0 and nota <= 10:
                    dados.append(nota)
                    return (f"Nota adicionada ao aluno {nome}.")
                else:
                    print("Erro! Digite um número de 0 a 10")
            except:
                print("Erro! Digite um número!")

    else:
        return (f"Erro! Tente digitar uma das opções: {opcoes}")

notas = []
nome = str(input("Digite o nome do Aluno: "))

while True:
    choice = str(input("O que você deseja fazer? "))
    funcao = opcao(choice=choice, dados=notas, nome=nome)
    if funcao[0] == "sair":
        print(funcao[1])
        break
    else:
        print(funcao)