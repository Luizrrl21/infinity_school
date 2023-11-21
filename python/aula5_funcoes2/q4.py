def imprimir_cores(lista_cores):
    for cor in lista_cores:
        print(cor, end=' ')

# Lista de cores
cores = ['\033[36m', 'azul', '\033[0;0m', '\033[32m', 'verde', '\033[0;0m', '\033[33m', 'amarelo', '\033[0;0m']

# Chamando a função
imprimir_cores(cores)