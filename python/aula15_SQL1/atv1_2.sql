CREATE DATABASE IF NOT EXISTS escola2;
USE escola2;

CREATE TABLE alunos(
	matricula INT PRIMARY KEY AUTO_INCREMENT,
    nome VARCHAR(100),
    idade INT,
    endereco VARCHAR(255)
);

CREATE TABLE professores(
	matricula INT PRIMARY KEY AUTO_INCREMENT,
    nome VARCHAR(100),
    especialidade VARCHAR(50),
    endereco VARCHAR(255)
);

CREATE TABLE turma(
	id INT PRIMARY KEY AUTO_INCREMENT,
    horario TIME,
    dia INT
);

CREATE TABLE disciplina(
	id INT PRIMARY KEY AUTO_INCREMENT,
    nome VARCHAR(50),
	qtd_aulas INT
)
