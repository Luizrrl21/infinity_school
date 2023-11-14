#Questão 2
#Dado o Dicionário Animal com a seguinte estrutura: {"Especie": "Cachorro", "Raça": "Pinscher", "Idade": 1, "Adestrado": "Sim"},
#faça um programa que cheque se o cachorro tem mais de 2 anos de idade, se tiver, crie uma nova chave chamada "Vacinado" e atribua o valor de
#verdadeiro, caso contrário, mude o valor da chave "Adestrado" para "Não"

dog = {
    "Especie": str(input("Espécie: ")),
    "Raça": str(input("Raça: ")),
    "Idade": int(input("Idade: ")),
    "Adestrado": bool(input("Adestrado: "))
    }

if dog["Idade"] > 2:  
    dog["Vacinado"] = True
else:
    dog["Adestrado"] = "Não"

print(dog)