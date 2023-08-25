class Estoque:

    def __init__(self):
        self.produtos = {}
    
    def registrar_produto(self, nome, preco, quantidade):
        if nome in self.produtos:
            self.produtos[nome]['quantidade'] += quantidade
        else:
            self.produtos[nome] = {'preco': preco, 'quantidade': quantidade}
  

    def listar_produtos_ordenados(self):
        valor_total = 0
        for produto, info in self.produtos.items():
            valor_total += info['preco'] * info['quantidade']

        return valor_total, sorted(self.produtos.items())
        
    

def tela():
    estoque = Estoque()
    
    while True:
        print("Controle de Estoque")
        print("1 - Registrar novo produto")
        print("2 - Listar produtos em ordem alfabética")
        print("3 - Sair")
        
        escolha = input("Escolha uma opção: ")
        
        if escolha == '1':
            nome = input("Nome do produto: ")
            preco = float(input("Preço do produto: "))
            quantidade = int(input("Quantidade: "))
            estoque.registrar_produto(nome, preco, quantidade)
            print(f"{quantidade} unidades de {nome} foram adicionadas ao estoque.")
        elif escolha == '2':
            valor_total = estoque.listar_produtos_ordenados()
            print(f"O valor total do estoque é R${valor_total:.2f}")
            produtos_ordenados = estoque.listar_produtos_ordenados()
            for produto, info in produtos_ordenados:
                print(f"{produto}: Preço R${info['preco']:.2f}, Quantidade: {info['quantidade']}")
        elif escolha == '3':
            print("Encerrando o programa.")
            break
        else:
            print("Opção inválida. Tente novamente.")


tela()
