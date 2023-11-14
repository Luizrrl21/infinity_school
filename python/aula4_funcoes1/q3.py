def valhora(valor: float, hora: int = 8):
    return round(valor/hora,2)

valor = float(input("Digite o valor em R$: "))
hora = int(input("Digite a quantidade de hora: "))
print(f"O valor da hora trabalhada é R${valhora(valor, hora)}")

