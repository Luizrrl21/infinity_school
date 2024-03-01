import mysql.connector

db_config = {
    "host": "localhost",
    "user": "root",
    "password": "Infinity102030",
    "database": "locadora"
}

nome = str(input("Digite o nome do filme: "))
genero = str(input("Digite o genero do filme: "))
ano = str(input("Digite o ano do filme: "))

def add(nome, genero, ano):
    conexao = mysql.connector.connect(**db_config)
    cursor = conexao.cursor()
    cursor.execute(f"INSERT INTO filmes(titulo, genero, ano_lanc) VALUES ('{nome}', '{genero}', '{ano}');")
    conexao.commit()
    cursor.close()
    conexao.close()
    print("Dados enviados ao bd")

def ver():
    conexao = mysql.connector.connect(**db_config)
    cursor = conexao.cursor()
    cursor.execute(f"SELECT * FROM filmes")
    lista = cursor.fetchall()
    cursor.close()
    conexao.close()
    print(lista)

add(nome, genero, ano)
ver()