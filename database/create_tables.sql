CREATE DATABASE combustiveis_anp;

USE combustiveis_anp;

CREATE TABLE preco_combustivel (
    id INT AUTO_INCREMENT PRIMARY KEY,
    regiao VARCHAR(10),
    estado VARCHAR(2),
    municipio VARCHAR(100),
    revenda VARCHAR(255),
    cnpj VARCHAR(20),
    produto VARCHAR(50),
    data_coleta DATE,
    valor_venda DECIMAL(10,3),
    valor_compra DECIMAL(10,3),
    bandeira VARCHAR(100)
);