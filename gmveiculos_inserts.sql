INSERT INTO condicoes_veiculos (condicao_usado, ano, leiloado, quilometragem) VALUES
(true, 2018, false, 50000),
(false, 2020, false, 10000),
(true, 2015, false, 80000),
(true, 2017, false, 60000),
(false, 2019, false, 15000),
(true, 2016, false, 70000);

INSERT INTO marcas (nome) VALUES
('Chevrolet'),
('Ford'),
('Volkswagen'),
('Toyota'),
('Honda'),
('Hyundai');

INSERT INTO modelos (nome, tipo, marca_id) VALUES
('Onix', 'carro', 1),
('Ka', 'carro', 2),
('Gol', 'carro', 3),
('Corolla', 'caroo', 4),
('Civic', 'carro', 5),
('HB20', 'carro', 6);

INSERT INTO veiculos (preco, pagamento, imagem, modelo_id, condicao_id) VALUES
(45000.00, 'À vista', 'carro_test.jpeg', 1, 1),
(35000.00, 'Financiado', 'carro_test.jpeg', 2, 2),
(30000.00, 'À vista', 'carro_test.jpeg', 3, 3),
(55000.00, 'Financiado', 'carro_test.jpeg', 4, 4),
(40000.00, 'À vista', 'carro_test.jpeg', 5, 5),
(32000.00, 'Financiado', 'carro_test.jpeg', 6, 6);

INSERT INTO interesse_venda (nome, telefone, email, mensagem, imagem) VALUES
('João Silva', '987654321', 'joao@email.com', 'Tenho interesse em vender meu veículo.', 'carro_test.jpeg'),
('Carlos Santos', '987654321', 'carlos@email.com', 'Tenho interesse em vender meu veículo.', 'carro_test.jpeg');

INSERT INTO interesse_compra (nome, telefone, email, mensagem, veiculo_id) VALUES
('Maria Souza', '987654321', 'maria@email.com', 'Tenho interesse em comprar um veículo.', 1),
('Ana Oliveira', '987654321', 'ana@email.com', 'Tenho interesse em comprar um veículo.', 2);