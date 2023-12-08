opcoes = ["add", "del", "edit", "see"]
bd = []

while True:
    acao = str(input("O que você deseja fazer? "))
    if acao == "add":
        produto = {
                "name": str(input("Nome do Produto: ")),
                "price": float(input("Preço do Produto: R$")),
                "qtd" : int(input("Quantidade do Produto: "))
            }
        bd.append(produto)
    elif acao == "del":
        