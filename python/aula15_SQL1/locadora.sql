CREATE DATABASE IF NOT EXISTS locadora;
USE locadora;

CREATE TABLE filmes(
	id INT PRIMARY KEY AUTO_INCREMENT,
    nome VARCHAR(50),
    genero VARCHAR(50),
    duracao int
);

CREATE TABLE jogos(
	id INT PRIMARY KEY AUTO_INCREMENT,
    nome VARCHAR(50),
    categoria VARCHAR(50),
    qtd_jogadores int
);

CREATE TABLE series(
	id INT PRIMARY KEY AUTO_INCREMENT,
    nome VARCHAR(50),
    genero VARCHAR(50),
	qtd_temporadas int
);

CREATE TABLE aluguel_filme(
	id INT PRIMARY KEY AUTO_INCREMENT,
    id_filme INT,
    FOREIGN KEY (id_filme) REFERENCES filmes(id),
    horario TIME,
    valor float
);

CREATE TABLE aluguel_jogos(
	id INT PRIMARY KEY AUTO_INCREMENT,
    id_jogo INT,
    FOREIGN KEY (id_jogo) REFERENCES jogos(id),
    horario TIME,
    valor float
);

CREATE TABLE aluguel_series(
	id INT PRIMARY KEY AUTO_INCREMENT,
    id_serie INT,
    FOREIGN KEY (id_serie) REFERENCES series(id),
    horario TIME,
    valor float
)   