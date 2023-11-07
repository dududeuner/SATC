CREATE TABLE Produtos (
    Codigo INT PRIMARY KEY,
    Descricao CHAR(255),
    ValorUnitario NUMERIC(10, 2),
    Ativo CHAR(1)
);


CREATE TABLE Marcas (
    Codigo INT PRIMARY KEY,
    Descricao VARCHAR(255)
);



ALTER TABLE Produtos
ADD CodigoMarca INT;


ALTER TABLE Produtos
ADD CONSTRAINT FK_Produtos_Marca FOREIGN KEY (CodigoMarca)
REFERENCES Marcas(Codigo);


ALTER TABLE Produtos
ALTER COLUMN CodigoMarca INT NOT NULL;


ALTER TABLE Produtos
ADD CONSTRAINT CK_Produtos_Ativo_Novo CHECK (Ativo IN ('S', 'N'));