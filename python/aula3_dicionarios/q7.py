#QUESTÃO 2
#Dado o conjunto Modulos com a seguinte estrutura {"Lógica de progamação", "Python", "HTML e CSS", "Javascript"}
#faça um programa que peça ao usuário o nome de um novo módulo e adicione esse módulo dentro desse conjunto

modulos = {"Lógica de progamação", "Python", "HTML e CSS", "Javascript"}
modulos.add(str(input("Digite o nome do novo módulo: ")))
print(modulos)