class No: # 1. Implemente todas as operaçoes mostradas nos pseudocodigos dos slides anteriores.
    def __init__(self, valor):
        self.valor = valor
        self.proximo = None

class ListaEncadeada:
    def __init__(self):
        self.primeiro = None

    def mostraNo(self, valor):
        print(valor)

    def inserirInicio(self, valor):
        novo = No(valor)
        novo.proximo = self.primeiro
        self.primeiro = novo

    def mostrar(self):
        if self.primeiro is None:
            print("Erro de lista vazia")
            return
        atual = self.primeiro
        while atual is not None:
            self.mostraNo(atual.valor)
            atual = atual.proximo

    def excluirInicio(self):
        if self.primeiro is None:
            print("Erro de lista vazia")
            return
        temp = self.primeiro
        self.primeiro = self.primeiro.proximo
        return temp

    def pesquisar(self, valor):
        if self.primeiro is None:
            print("Erro de lista vazia")
            return
        atual = self.primeiro
        while atual.valor != valor:
            if atual.proximo is None:
                return None
            atual = atual.proximo
        return atual

    def excluirQualquer(self, valor):
        if self.primeiro is None:
            print("Erro de lista vazia")
            return
        atual = self.primeiro
        anterior = self.primeiro
        while atual.valor != valor:
            if atual.proximo is None:
                return None
            else:
                anterior = atual
                atual = atual.proximo
        if atual == self.primeiro:
            self.primeiro = self.primeiro.proximo
        else:
            anterior.proximo = atual.proximo
        return atual
    
# 2. Implemente tambem a operaçao de inserçao ordenada de dados. R - inserirOrdenado()
def inserirOrdenado(lista, valor):
    novo = No(valor)
    if lista.primeiro is None or valor <= lista.primeiro.valor:
        novo.proximo = lista.primeiro
        lista.primeiro = novo
        return
    atual = lista.primeiro
    while atual.proximo is not None and atual.proximo.valor < valor:
        atual = atual.proximo
    novo.proximo = atual.proximo
    atual.proximo = novo



# 3. Considere uma Lista Encadeada Simples vazia. Insira no início da lista a sequência de valores 3, 7 e 6. Demonstre de forma detalhada (desenho) a inserção dos nos e a inserçao e sobrescrita dos ponteiros

lista = ListaEncadeada()
lista.inserirInicio(3)
lista.inserirInicio(7)
lista.inserirInicio(6)
lista.mostrar()

# 4. Considere uma Lista Encadeada Simples contendo a partir do seu início os elementos 1, 5, 3 e 2. Desenhe a lista e faça a exclusão do elemento 3 através do preenchimento da Tabela abaixo. Demonstre através de desenho os detalhes da exclusão do elemento solicitado.
# VALOR | ATUAL | ANTERIOR
#   1       1      None
#   5       5       1
#   3       3       5

# 5. Onde é realizada a inserção de novos elementos em uma Lista Encadeada Simples?
# A inserçao de novos elementos em uma Lista Encadeada Simples geralmente é realizada no inicio da lista ou em posiçoes especificas, conforme necessario. 

# 6. Qual o nome da estrutura que a Lista Encadeada Simples utiliza para guardar seus dados?
#A estrutura que uma Lista Encadeada Simples utiliza para guardar seus dados é chamada de "nó" (ou "Node" em inglês). Cada nó contém o valor dos dados e um #ponteiro para o próximo nó na lista.

# 7. Qual critério é utilizado para saber se uma Lista Encadeada Simples está vazia?
#Para verificar se uma Lista Encadeada Simples esta vazia, se o ponteiro para o primeiro nó  é igual a None. Se for igual a None, a lista está vazia.

# 8. Qual criterio é utilizado para saber se o algoritmo de busca está no ultimo elemento de uma Lista Encadeada Simples?
#Para verificar se o algoritmo de busca está no último elemento de uma Lista Encadeada Simples, ele verifica se o ponteiro para o proximo ou next do "nó" atual é igual a None. Se for igual a None, significa que o nó atual é o ultimo elemento da lista.