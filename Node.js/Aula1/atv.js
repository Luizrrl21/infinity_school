const mysql = require("mysql");
const express = require("express");
const cors = require("cors");

const app = express();
const port = 3000;

app.use(cors());
app.use(express.json());

const connection = mysql.createConnection({
  host: "localhost",
  user: "root",
  password: "Mysql102030",
  database: "locadora",
});

connection.connect((err) => {
  if (err) {
    console.error("Erro ao se conectar com o banco, cheque os dados");
  } else {
    console.log("Conexão bem sucedida");
  }
});

app.get("/buscar_filmes", (req, res) => {
  connection.query("SELECT * FROM filmes", (err, results) => {
    if (err) {
      console.error("Error a executar a consulta", err);
      res.status(500).send("Erro interno no servidor");
    } else {
      res.json(results);
    }
  });
});

app.post("/inserir_filme", (req, res) => {
  const dados = req.body;
  connection.query(
    "INSERT INTO filmes (nome, genero, ano) VALUES (?, ?, ?)",
    [dados.campo_nome, dados.campo_genero, dados.campo_ano],
    (err, results) => {
      if (err) {
        console.error("Erro ao executar a consulta", err);
        res.status(500).send("Erro interno no servidor");
      } else {
        res.json({ mensagem: "Dados inseridos com sucesso" });
      }
    }
  );
});

app.listen(port, () => {
  console.log("Servidor iniciado com sucesso");
});