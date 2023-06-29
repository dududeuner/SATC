estoque = {}

opcao = None

while opcao != "0":
    print("\n===== Sistema de Gestão de Estoque =====")
    print("1. Adicionar novo produto")
    print("2. Atualizar quantidade de produto")
    print("3. Verificar disponibilidade de produto")
    print("4. Listar produtos em estoque")
    print("5. Remover produto do estoque")
    print("0. Sair do programa")
    
    opcao = input("Digite o número da opção desejada: ")
    
    if opcao == "1":
        nome = input("Digite o nome do produto: ")
        preco = float(input("Digite o preço do produto: "))
        quantidade = int(input("Digite a quantidade disponível: "))
        
        produto = {
            "preco": preco,
            "quantidade": quantidade
        }
        
        estoque[nome] = produto
        print("Produto adicionado ao estoque com sucesso!")
    
    elif opcao == "2":
        nome = input("Digite o nome do produto: ")
        
        if nome in estoque:
            quantidade = int(input("Digite a nova quantidade: "))
            estoque[nome]["quantidade"] = quantidade
            print("Quantidade atualizada com sucesso!")
        else:
            print("Produto não encontrado no estoque.")
    
    elif opcao == "3":
        nome = input("Digite o nome do produto: ")
        
        if nome in estoque:
            quantidade = estoque[nome]["quantidade"]
            print(f"O produto '{nome}' está disponível em estoque com quantidade {quantidade}.")
        else:
            print("Produto não encontrado no estoque.")
    
    elif opcao == "4":
        if len(estoque) > 0:
            print("Produtos em estoque:")
            for nome, produto in sorted(estoque.items()):
                preco = produto["preco"]
                quantidade = produto["quantidade"]
                print(f"Nome: {nome} | Preço: R${preco} | Quantidade: {quantidade}")
        else:
            print("Não há produtos em estoque.")
    
    elif opcao == "5":
        nome = input("Digite o nome do produto: ")
        
        if nome in estoque:
            del estoque[nome]
            print("Produto removido do estoque com sucesso!")
        else:
            print("Produto não encontrado no estoque.")
    
    elif opcao == "0":
        break
    
    else:
        print("Opção inválida. Tente novamente.")


quantidade_total = sum(produto["quantidade"] for produto in estoque.values())
valor_total = sum(produto["preco"] * produto["quantidade"] for produto in estoque.values())

print("\n===== Resumo do Estoque =====")
print(f"Quantidade total de produtos: {quantidade_total}")
print(f"Valor total do estoque: R${valor_total}")