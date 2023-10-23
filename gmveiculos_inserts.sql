-- Inserir dados na tabela condicoes_veiculos
INSERT INTO condicoes_veiculos (condicao_usado, ano, leiloado, quilometragem)
VALUES
    (TRUE, '2019', FALSE, 1000),
    (TRUE, '2020', FALSE, 573),
    (TRUE, '2015', TRUE, 9437),
    (FALSE, '2021', FALSE, 0);

-- Inserir dados na tabela marcas
INSERT INTO marcas (nome)
VALUES
    ('Toyota'),
    ('Honda'),
    ('Ford'),
    ('Volkswagen');

-- Inserir dados na tabela modelos
INSERT INTO modelos (nome, tipo, marca_id)
VALUES
    ('Corolla', 'carro', 1),
    ('Bis', 'moto', 2),
    ('Focus', 'carro', 3),
    ('Golf', 'carro', 4);

-- Inserir dados na tabela veiculos
INSERT INTO veiculos (preco, pagamento, modelo_id, condicao_id)
VALUES
    (25000.00, 'À vista', 1, 1),
    (22000.00, 'Financiamento', 2, 2),
    (15000.00, 'À vista', 3, 3),
    (18000.00, 'Financiamento', 4, 4);
    
-- Inserir dados na tabela interesse_venda
INSERT INTO interesse_venda (nome, telefone, email, mensagem)
VALUES
('Lucas', '1234567890', 'exemplo@email.com', 'Estou interessado neste veículo.');

-- Inserir dados na tabela interesse_venda_veiculos
INSERT INTO interesse_compra (nome, telefone, email, mensagem, veiculo_id)
VALUES
('João', '9876543210', 'exemplo2@email.com', 'Gostaria de mais informações sobre este veículo.', 1);