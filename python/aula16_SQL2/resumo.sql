CREATE DATABASE escola;
USE ESCOLA;

CREATE TABLE turma (
	id INT AUTO_INCREMENT PRIMARY KEY,
    nome VARCHAR(255),
    horario INT
);

CREATE TABLE alunos (
	id INT AUTO_INCREMENT PRIMARY KEY,
    nome VARCHAR(255),
    cpf VARCHAR(15),
    id_turma INT,
    FOREIGN KEY (id_turma) REFERENCES turma(id),
    idade INT
);

CREATE TABLE professores (
	id INT AUTO_INCREMENT PRIMARY KEY,
    nome VARCHAR(255),
    disciplina VARCHAR(50),
    id_turma INT,
    FOREIGN KEY (id_turma) REFERENCES turma(id)
);

ALTER TABLE turma MODIFY nome VARCHAR(100);
ALTER TABLE turma CHANGE nome titulo VARCHAR(15);
ALTER TABLE turma ADD  qtd_alunos INT;
ALTER TABLE turma DROP COLUMN qtd_alunos;