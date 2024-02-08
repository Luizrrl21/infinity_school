def cores(texto: str, cor:str):
    match cor.lower():
        case "red":
            return f"\033[0;49;31m{texto}\033[0;0m"
        case "green":
            return f"\033[0;49;32m{texto}\033[0;0m"
        case "yellow":
            return f"\033[0;49;33m{texto}\033[0;0m"
        case "blue":
            return f"\033[0;49;36m{texto}\033[0;0m"
        case "gray":
            return f"\033[0;49;90m{texto}\033[0;0m"
        case _:
            return texto

def total(lista:list):
    #Passa um loop por todos os valores da compra e retorna o Total
    sub_total = 0
    for i in lista:
        sub_total += i["subtotal"]

    return round(sub_total, 2)

def add(lista:list):
    #Produto
    produto = str(input("\033[0;49;90mProduto: \033[0;0m")).upper()

    #Quantidade com validação de Erro
    while True:
        try:
            quantidade = float(input("\033[0;49;90mQuantidade: \033[0;0m"))
            break
        except:
            print("\033[0;49;31mERRO! Digite um número\033[0;0m")

    #Preço com validação de Erro
    while True:
        try:
            preco = float(input("\033[0;49;90mPreço: \033[0;0m"))
            break
        except:
            print("\033[0;49;31mERRO! Digite um número\033[0;0m")
    
    #Cálculo do subtotal do Produto (qtd*price)
    subtotal = round(quantidade*preco,2)
    print(f"\033[0;49;90mValor:\033[0;0m R${subtotal}")
    print("")

    #Junção no dicionário
    dicionario = {
        "prod" : produto,
        "qtd" : quantidade,
        "price" : preco,
        "subtotal" : subtotal
    }

    #Adição na Lista
    lista.append(dicionario)
    print(f"\033[0;49;32m{dicionario['prod']} adicionado!\033[0;0m")

def ver(lista:list):
    for i in lista:
        print(f"""
        {cores("Produto: ","blue")}{i["prod"]}
        {cores("Quantidade: ","blue")}{i["qtd"]}
        {cores("Preço: ","blue")}{i["price"]}
        {cores("Valor: ","blue")}{i["subtotal"]}
""")
        
def att(lista:list):
    ajuste = str(input("Qual produto você quer alterar? "))
    achou = False
    for i in lista:
        if i["prod"] == ajuste:
            achou = True
            n_nome = str(input(cores("Novo nome:","gray")))
            n_qtd = float(input(cores("Nova Quantidade:","gray")))
            n_price = float(input(cores("Novo Preço:", "gray")))

            if n_nome != "":
                i["prod"] = n_nome
            if n_qtd != "":
                i["qtd"] = n_qtd
            if n_price != "":
                i["pric"] = n_price

