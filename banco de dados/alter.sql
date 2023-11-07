ALTER TABLE Produtos
ADD CONSTRAINT CK_Produtos_Ativo_Novo CHECK (Ativo IN ('S', 'N'));