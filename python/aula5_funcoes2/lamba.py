#Usando DEF
def saudacao1(nome):
    return f"Bom dia {nome}"

#Usando LAMDA
saudacao2 = lambda nome : f"Bom dia {nome}"

nome = "Luiz"

print(saudacao1(nome))
print(saudacao2(nome))