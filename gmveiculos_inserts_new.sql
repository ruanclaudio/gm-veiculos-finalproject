INSERT INTO condicoes_veiculos (condicao_usado, ano, leiloado, quilometragem) VALUES
-- (true, 2018, false, 50000),
-- (false, 2020, false, 10000),
-- (true, 2015, false, 80000),
-- (true, 2017, false, 60000),
-- (false, 2019, false, 15000),
-- (true, 2016, false, 70000), 
(true, 2019, false, 40000),
(true, 2020, false, 50000),
(false, 2023, false, 00000),
(false, 2023, false, 00000), 
(false, 2023, false, 00000),
(false, 2023, false, 00000),
(false, 2023, false, 00000),
(false, 2023, false, 00000),
(false, 2023, false, 00000),
(true, 2017, false, 50000),
(true, 2018, true, 78000);

INSERT INTO marcas (nome) VALUES
('Chevrolet'), -- 1
('Ford'), -- 2
('Volkswagen'), -- 3
('Toyota'), -- 4
('Honda'), -- 5
('Hyundai'), -- 6
('Fiat'), -- 7
('Yamaha'); -- 8
INSERT INTO modelos (nome, tipo, marca_id) VALUES
-- ('Onix', 'carro', 1),
-- ('Ka', 'carro', 2),
-- ('Gol', 'carro', 3),
-- ('Corolla', 'caroo', 4),
-- ('Civic', 'carro', 5),
-- ('HB20', 'carro', 6),
('Palio', 'carro', 7),
('Uno', 'carro', 7),
('NXR 160 Bros ESDD', 'moto', 5),
('PCX CBS', 'moto', 5),
('Pop 110i','moto', 5),
('Biz 125', 'moto', 5),
('CG 160 Titan', 'moto', 5),
('Fazer 150 UBS','moto', 8),
('Lander 250 ABS','moto', 8),
('CG fan 160','moto', 5),
('Hilux', 'carro', 4);

INSERT INTO veiculos (preco, pagamento, imagem, modelo_id, condicao_id) VALUES
-- (45000.00, 'À vista', 'carro_test.jpeg', 1, 1),
-- (35000.00, 'Financiado', 'carro_test.jpeg', 2, 2),
-- (30000.00, 'À vista', 'carro_test.jpeg', 3, 3),
-- (55000.00, 'Financiado', 'carro_test.jpeg', 4, 4),
-- (40000.00, 'À vista', 'carro_test.jpeg', 5, 5),
-- (32000.00, 'Financiado', 'carro_test.jpeg', 6, 6),
(40000.00, 'Financiado','palio-2019-usado-prata-23.jpeg', 7, 7),
(42000.00, 'À vista','fiat-uno-2020-branco-usado-2335.webp', 7, 7),
(18686.00, 'À vista','NXR-BROSS-160-nova-vermelha-2.jpeg', 5, 5),
(16800.00, 'À vista','PCX-2024-nova-1.jpeg', 5, 5),
(9730.00, 'À vista','pop-110-nova-branca-3.jpeg', 5, 5),
(14320.00, 'À vista','biz-125-nova-branca-4.jpeg', 5, 5),
(16760.00, 'À vista','CG-titan-nova-5.jpeg', 5, 5),
(16500.00, 'À vista','fazer-150-nova-roxo-6.jpeg', 8, 8),
(23000.00, 'financiado','lander-250-nova-vermelha-7.jpeg', 8, 8),
(23000.00, 'consorcio','lander-250-nova-vermelha-7.jpeg', 8, 8),
(10000.00, 'Consorcio','CG-fan-160-2017-usada-vermelha-89.jpg', 5, 5),
(70000.00, 'Financiado','toyota-hilux-2018-prata-145.webp', 4, 4);



INSERT INTO interesse_venda (nome, telefone, email, mensagem, imagem) VALUES
('João Silva', '987654321', 'joao@email.com', 'Tenho interesse em vender meu veículo.', 'carro_test.jpeg'),
('Carlos Santos', '987654321', 'carlos@email.com', 'Tenho interesse em vender meu veículo.', 'carro_test.jpeg');

INSERT INTO interesse_compra (nome, telefone, email, mensagem, veiculo_id) VALUES
('Maria Souza', '987654321', 'maria@email.com', 'Tenho interesse em comprar um veículo.', 1),
('Ana Oliveira', '987654321', 'ana@email.com', 'Tenho interesse em comprar um veículo.', 2);