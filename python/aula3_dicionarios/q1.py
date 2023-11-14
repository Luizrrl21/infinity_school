#Questão 1
#Dado O Dicionário pessoa com a seguinte estrutura: {"Nome": "Abel", "Idade": 28, "Altura": 1.79, "Habilitacao": True},
#faça um programa que imprima na tela quantas chaves existem nesse dicionário, e quais os nomes de cada uma delas

pessoa = {
    "Nome": "Abel",
    "Idade": 28,
    "Altura": 1.79,
    "Habilitacao": True
    }

quantidade = len(pessoa)
print(f"Existem {quantidade} chaves e são:")

for i in pessoa:
    print(i)