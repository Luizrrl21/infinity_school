CREATE DATABASE registros;
USE registros;

CREATE TABLE pessoas(
	id INT PRIMARY KEY,
    nome_completo VARCHAR(255),
    idade INT,
    genero VARCHAR(9),
    nacionalidade VARCHAR(50),
    email VARCHAR(50),
    estado_civil VARCHAR(50),
    nome_pai VARCHAR(255),
    nome_mae VARCHAR(255)
);

INSERT INTO pessoas (id, nome_completo, idade, genero, nacionalidade, email, estado_civil, nome_pai, nome_mae) VALUES (
	1, "Luiz Roberto Rodrigues Leitão", 22, "Masculino", "Brasileiro(a)", "luiz@masterrepr.com.br", "casado(a)", "Herlanerson", "Carla"
);

INSERT INTO pessoas (id, nome_completo, idade, genero, nacionalidade, email, estado_civil, nome_pai, nome_mae) VALUES (
	2, "Maria Vitória Santos Leitão", 1, "Feminino", "Brasileiro(a)", "teste@gmail.com", "solteiro(a)", "Luiz Roberto Rodrigues Leitão", "Niuzilene"
);

INSERT INTO pessoas (id, nome_completo, idade, genero, nacionalidade, email, estado_civil, nome_mae) VALUES (
	3, "Niuzilene Santos do Nascimento", 23, "Feminino", "Brasileiro(a)", "teste2@gmail.com", "casado(a)", "Edileusa"
);

UPDATE pessoas SET id = 9, idade =21  WHERE id = 1;
DELETE FROM pessoas WHERE id =9;

SELECT * FROM pessoas