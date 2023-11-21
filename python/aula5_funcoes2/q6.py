p1 = str(input("Primeira palavra: "))
p2 = str(input("Segunda palavra: "))

verifica = lambda str1, str2 : f"{str1}-{str2}" if len(str1) > 5 and len(str2) > 5 else "Erro!"

print(verifica(p1, p2))