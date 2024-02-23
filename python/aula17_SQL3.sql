CREATE DATABASE escola;
USE escola;

CREATE TABLE professores(
	id INT AUTO_INCREMENT PRIMARY KEY,
    nome NVARCHAR(255),
    disciplina NVARCHAR(50)
);

CREATE TABLE turma(
	id INT AUTO_INCREMENT PRIMARY KEY,
    horario TIME,
    id_professor INT,
    FOREIGN KEY (id_professor) REFERENCES professores(id)
);

CREATE TABLE alunos(
	id INT AUTO_INCREMENT PRIMARY KEY,
    nome NVARCHAR(255),
    cpf CHAR(11),
    endereco NVARCHAR(255),
    id_turma INT,
    FOREIGN KEY (id_turma) REFERENCES turma(id)
);

INSERT INTO professores(nome, disciplina) VALUES
("Abel", "Programação"),
("Pryscila", "Marketing");

INSERT INTO turma(horario, id_professor) VALUES
("15:30:00", 1),
("19:00:00", 2);

INSERT INTO alunos(nome, cpf, endereco, id_turma) VALUES
("Luiz", "12312312312", "asdkasdjasdads", 1),
("Nyl", "12312312312", "asdkasdjasdads", 2),
("Maria", "12312312312", "asdkasdjasdads", 2),
("Herlanerson", "12312312312", "asdkasdjasdads", 2),
("Carla", "12312312312", "asdkasdjasdads", 2);

UPDATE alunos SET nome = "Mavi"  WHERE id = 3;
DELETE FROM alunos WHERE id = 4;
SELECT * FROM alunos;
