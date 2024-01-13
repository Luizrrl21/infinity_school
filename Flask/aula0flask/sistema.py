def cadastro(login, senha):
    usuarios[login] = senha

usuarios = {}

cadastro("Luiz", 8127381)
print(usuarios)