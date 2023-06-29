import json
import os

requisitos = {}

def adicionar_requisito():
    id_requisito = input("ID do requisito: ")
    nome = input("Nome do requisito: ")
    descricao = input("Descrição do requisito: ")
    prioridade = input("Prioridade do requisito: ")
    status = input("Status do requisito: ")
    tipo = input("Tipo do requisito (funcional ou não funcional): ")

    requisito = {
        'nome': nome,
        'descricao': descricao,
        'prioridade': prioridade,
        'status': status,
        'tipo': tipo
    }
    requisitos[id_requisito] = requisito
    print("Requisito adicionado com sucesso!")

def exibir_requisitos():
    for id_requisito, requisito in requisitos.items():
        print("-----------------------")
        print(f"=== Requisito {id_requisito} ===")
        print(f"Nome: {requisito['nome']}")
        print(f"Descrição: {requisito['descricao']}")
        print(f"Prioridade: {requisito['prioridade']}")
        print(f"Status: {requisito['status']}")
        print(f"Tipo: {requisito['tipo']}")
        print("-----------------------")

def deletar_requisito():
    print("Requisitos disponíveis para deletar:")
    exibir_requisitos()
    id_requisito = input("Digite o ID do requisito que deseja deletar: ")
    if id_requisito in requisitos:
        del requisitos[id_requisito]
        print("Requisito deletado com sucesso!")
    else:
        print("ID do requisito não encontrado.")

def alterar_requisito():
    print("Requisitos disponíveis para alterar:")
    exibir_requisitos()
    id_requisito = input("Digite o ID do requisito que deseja alterar: ")
    if id_requisito in requisitos:
        requisito = requisitos[id_requisito]
        nome = input("Nome do requisito: ")
        descricao = input("Descrição do requisito: ")
        prioridade = input("Prioridade do requisito: ")
        status = input("Status do requisito: ")
        tipo = input("Tipo do requisito (funcional ou não funcional): ")

        requisito['nome'] = nome
        requisito['descricao'] = descricao
        requisito['prioridade'] = prioridade
        requisito['status'] = status
        requisito['tipo'] = tipo

        print("Requisito alterado com sucesso!")
    else:
        print("ID do requisito não encontrado.")

def salvar_requisitos():
    diretorio_atual = os.path.dirname(os.path.abspath(__file__))
    caminho_arquivo = os.path.join(diretorio_atual, "requisitos.json")
    with open(caminho_arquivo, 'w') as arquivo:
        json.dump(requisitos, arquivo)
    print("Requisitos salvos com sucesso!")

def carregar_requisitos():
    diretorio_atual = os.path.dirname(os.path.abspath(__file__))
    caminho_arquivo = os.path.join(diretorio_atual, "requisitos.json")
    try:
        with open(caminho_arquivo, 'r') as arquivo:
            requisitos.update(json.load(arquivo))
        print("Requisitos carregados com sucesso!")
    except FileNotFoundError:
        print("Nenhum arquivo de requisitos encontrado.")

carregar_requisitos()

while True:
    print("=== Sistema de Gestão de Requisitos ===")
    print("1. Adicionar Requisito")
    print("2. Exibir requisito")
    print("3. Alterar Requisito")
    print("4. Deletar Requisito")
    print("0. Sair")
    print("---------------------------------------")
    opcao = input("Escolha uma opção: ")

    if opcao == "1":
        adicionar_requisito()
    elif opcao == "2":
        exibir_requisitos()
    elif opcao == "3":
        alterar_requisito()
    elif opcao == "4":
        deletar_requisito()
    elif opcao == "0":
        salvar_requisitos()
        break
    else:
        print("Opção inválida!")

print("Programa encerrado.")