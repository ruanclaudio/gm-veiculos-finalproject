CREATE DATABASE gmveiculos;
USE gmveiculos;

CREATE TABLE condicoes_veiculos (
	id INT PRIMARY KEY AUTO_INCREMENT,
	condicao_usado BOOLEAN NOT NULL,
	ano YEAR NOT NULL,
	leiloado BOOLEAN NOT NULL
);

CREATE TABLE marcas (
	id INT PRIMARY KEY AUTO_INCREMENT,
	nome VARCHAR(50) NOT NULL
);

CREATE TABLE modelos (
	id INT PRIMARY KEY AUTO_INCREMENT,
	nome VARCHAR(50) NOT NULL,
	tipo VARCHAR(50) NOT NULL,

	marca_id INT NOT NULL,

	FOREIGN KEY (marca_id) REFERENCES marcas(id)
);

CREATE TABLE veiculos (
	id INT PRIMARY KEY AUTO_INCREMENT,
	preco DECIMAL(10, 2) NOT NULL,
	pagamento VARCHAR(50) NOT NULL,

	modelo_id INT NOT NULL,
	condicao_id INT NOT NULL,

	FOREIGN KEY (modelo_id) REFERENCES modelos(id),
	FOREIGN KEY (condicao_id) REFERENCES condicoes_veiculos(id)
);

CREATE TABLE interesse_venda (
	id INT PRIMARY KEY AUTO_INCREMENT,
    nome VARCHAR(100) NOT NULL,
	telefone VARCHAR(11) NOT NULL,
    email VARCHAR(150) NOT NULL,
    mensagem VARCHAR(1000) NOT NULL
);

CREATE TABLE interesse_compra (
	id INT PRIMARY KEY AUTO_INCREMENT,
    nome VARCHAR(100) NOT NULL,
	telefone VARCHAR(11) NOT NULL,
    email VARCHAR(150) NOT NULL,
    mensagem VARCHAR(1000) NOT NULL,
    
    veiculo_id INT NOT NULL,
    
    FOREIGN KEY (veiculo_id) REFERENCES veiculos(id)
);