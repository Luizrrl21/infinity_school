# [LP-A02] Escreva um programa em python que pergunte ao usuário a velocidade de um carro.
#Caso ultrapasse 80 km/h, exiba uma mensagem dizendo que o usuário foi multado.
#Nesse caso, exiba o valor da multa, cobrando R$20,00 por cada km que exceder 80 km/h.

v_carro = int(input("Velocidade do carro em 'km/h': "))
v_padrao = 80
v_dif = float(v_carro - v_padrao)

if v_carro > v_padrao:
    print(f"Velocidade acima do máximo permitido (80km/h), aplicar multa de R${v_dif*20}")
else:
    print(f"A velocidade está dentro do adequado!")