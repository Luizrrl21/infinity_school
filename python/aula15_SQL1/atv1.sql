CREATE DATABASE IF NOT EXISTS escola;
USE escola;

CREATE TABLE alunos(
	id_aluno INT PRIMARY KEY AUTO_INCREMENT,
	nome VARCHAR(255),
    idade INT
);

CREATE TABLE cursos(
	id_curso INT PRIMARY KEY AUTO_INCREMENT,
    nome_curso VARCHAR(50),
    carga_horaria INT
);

DROP TABLE matriculas;
CREATE TABLE matriculas(
	id_matricula INT PRIMARY KEY AUTO_INCREMENT,
    id_aluno INT,
    FOREIGN KEY (id_aluno) REFERENCES alunos(id_aluno),
    id_curso INT,
    FOREIGN KEY (id_curso) REFERENCES cursos(id_curso),
    data_matricula DATE
)