o1 = float(input("Valor do orçamento 1:"))
o2 = float(input("Valor do orçamento 2:"))
o3 = float(input("Valor do orçamento 3:"))


if o1 < o2 and o1 < o3:
    print(f"Opte pelo orçamento 1 com valor de R${o1}, pois é o mais barato!")
elif o2 < o1 and o2 < o3:
    print(f"Opte pelo orçamento 2 com valor de R${o2}, pois é o mais barato!")
elif o3 < o1 and o3 < o2:
    print(f"Opte pelo orçamento 3 com valor de R${o3}, pois é o mais barato!")
elif o1 == o2 and o1 == o3:
    print(f"Todos os orçamentos tem o mesmo valor (R${o1}), escolha qualquer um")

