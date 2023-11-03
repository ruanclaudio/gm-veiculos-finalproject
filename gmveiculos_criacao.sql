CREATE DATABASE gmveiculos;
USE gmveiculos;

CREATE TABLE condicoes_veiculos (
	id INT PRIMARY KEY AUTO_INCREMENT,
	condicao_usado BOOLEAN NOT NULL,
	ano YEAR NOT NULL,
	leiloado BOOLEAN NOT NULL,
    quilometragem INT NOT NULL
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
    porcentagem_desconto INT,
    imagem VARCHAR(100),

	modelo_id INT NOT NULL,
	condicao_id INT NOT NULL,

	FOREIGN KEY (modelo_id) REFERENCES modelos(id),
	FOREIGN KEY (condicao_id) REFERENCES condicoes_veiculos(id)
);

CREATE TABLE interesse_venda (
	id INT PRIMARY KEY AUTO_INCREMENT,
    nome VARCHAR(100) NOT NULL,
	telefone VARCHAR(13) NOT NULL,
    email VARCHAR(150) NOT NULL,
    mensagem VARCHAR(1000) NOT NULL,
    imagem VARCHAR(100)
);

CREATE TABLE interesse_compra (
	id INT PRIMARY KEY AUTO_INCREMENT,
    nome VARCHAR(100) NOT NULL,
	telefone VARCHAR(13) NOT NULL,
    email VARCHAR(150) NOT NULL,
    mensagem VARCHAR(1000) NOT NULL,
    estado VARCHAR(50) DEFAULT "Não Analisado",
    
    veiculo_id INT NOT NULL,
    
    FOREIGN KEY (veiculo_id) REFERENCES veiculos(id)
);

CREATE TABLE promocoes (
	id INT PRIMARY KEY AUTO_INCREMENT,
    nome VARCHAR(100) NOT NULL,
    imagem_banner VARCHAR(100),
    ativa BOOLEAN NOT NULL DEFAULT 0
);