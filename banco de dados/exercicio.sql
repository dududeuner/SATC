analises: descritiva, diagnostica, preditiva e prescritiva


CRUD
Create
Read
Update
Delete


estruturado - SQL
semi-estruturado - JSON
nao estruturado - Midias



EX01

(uma tabela com consumo a cada de cerveja a cada mes e a temperatura media de cada mes)

dados: temperatura do mes e consumo em cerveja do mes

informaçoes: quanto mais quente for o mes mais consumo de cerveja, fevereiro o mes com mais consumo
julho o com menos, janeiro o mes mais quente, julho o mais frio, 4,851 cervejas vendidas no ano, a temperatura media do ano
foi 24,4 graus, media de consumo anual mensal.



descritiva: dados do passado, fevereiro o mes com mais consumo, julho o com menos, janeiro o mes mais quente, julho o mais frio,
4,851 cervejas vendidas no ano, a temperatura media do anofoi 24,4 graus, media de consumo anual mensal.


diagnostica: indentificar problemas, fevereiro muita gente bebada


preditiva: previsoes futuras, quanto mais quente mais consumo


prescritiva: acoes recomendadas, promocoes para o mes mais vendido e o com menos vendas






SCRIPT DIA 10/10 SQL



CREATE TABLE cliente (
    cod_cliente INT PRIMARY KEY,
    nome VARCHAR(50),
    cpf CHAR(11),
    sexo CHAR(1),
    endereco VARCHAR(200),
    telefone_fixo VARCHAR(10),
    telefone_celular VARCHAR(11)
);

CREATE TABLE apolice (
    cod_apolice INT PRIMARY KEY,
    cod_cliente INT,
    data_inicio_vigencia DATE,
    data_fim_vigencia DATE,
    valor_cobertura NUMERIC(10,2),
    valor_franquia NUMERIC(10,2),
    placa CHAR(10),
    CONSTRAINT fk_cliente__apolice FOREIGN KEY (cod_cliente) REFERENCES cliente(cod_cliente),
    CONSTRAINT fk_carro__apolice FOREIGN KEY (placa) REFERENCES carro(placa)
);

CREATE TABLE sinistro (
    cod_sinistro INT PRIMARY KEY,
    placa CHAR(10),
    data_sinistro DATE,
    hora_sinistro TIME,
    local_sinistro VARCHAR(100),
    condutor VARCHAR(50),
    CONSTRAINT fk_carro__sinistro FOREIGN KEY (placa) REFERENCES carro(placa)
);

CREATE TABLE carro (
    placa CHAR(10) PRIMARY KEY,
    modelo VARCHAR(50),
    chassi VARCHAR(30),
    marca VARCHAR(30),
    ano TINYINT,
    cor VARCHAR(10)
);

ALTER TABLE sinistro
ADD CONSTRAINT fk_cliente__sinistro FOREIGN KEY (placa) REFERENCES carro(placa);