#Supondo que a população de um país A seja da ordem de 80000 habitantes com uma
#taxa anual de crescimento de 3% e que a população de B seja 200000 habitantes com
#uma taxa de crescimento de 1.5%. Faça um programa que calcule e escreva o número de
#anos necessários para que a população do país A ultrapasse ou iguale a população do
#país B, mantidas as taxas de crescimento.

a_qtd = 80000
a_tx = 3/100
b_qtd = 200000
b_tx = 1.5/100

ano = 0

while True:
    ano = ano + 1
    a_qtd = int((a_qtd * a_tx) + a_qtd)
    b_qtd = int((b_qtd * b_tx) + b_qtd)
    if a_qtd >= b_qtd:
        break

print(f"Levaram {ano} anos para a população A ({a_qtd} habitantes) superar a população B ({b_qtd} habitantes)")