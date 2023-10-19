-- Inserir dados na tabela condicoes_veiculos
INSERT INTO condicoes_veiculos (condicao_novo, ano, cor, quilometragem, leiloado)
VALUES
    (TRUE, '2019', 'Prata', 25000, FALSE),
    (TRUE, '2020', 'Preto', 15000, FALSE),
    (TRUE, '2015', 'Vermelho', 80000, TRUE),
    (FALSE, '2021', 'Branco', 10000, FALSE);

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
    ('Corolla', 'Sedan', 1),
    ('Civic', 'Sedan', 2),
    ('Focus', 'Hatchback', 3),
    ('Golf', 'Hatchback', 4);

-- Inserir dados na tabela veiculos
INSERT INTO veiculos (preco, pagamento, modelo_id, condicao_id)
VALUES
    (25000.00, 'À vista', 1, 1),
    (22000.00, 'Financiamento', 2, 2),
    (15000.00, 'À vista', 3, 3),
    (18000.00, 'Financiamento', 4, 4);
    
-- Inserir dados na tabela interesse_venda
INSERT INTO interesse_venda (telefone, email, mensagem)
VALUES
('1234567890', 'exemplo@email.com', 'Estou interessado neste veículo.');

-- Inserir dados na tabela interesse_venda_veiculos
INSERT INTO interesse_compra (telefone, email, mensagem, veiculo_id)
VALUES
('9876543210', 'exemplo2@email.com', 'Gostaria de mais informações sobre este veículo.', 1);