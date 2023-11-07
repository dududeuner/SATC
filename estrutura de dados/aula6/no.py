class No():

  def __init__(self, pValor):
    self.__valor = pValor
    self.__proximo = None
    self.__anterior = None

  @property
  def valor(self):
    return self.__valor

  @property
  def anterior(self):
    return self.__anterior

  @anterior.setter
  def anterior(self, pAnterior):
    self.__anterior = pAnterior

  @property
  def proximo(self):
    return self.__proximo

  @proximo.setter
  def proximo(self, pProximo):
    self.__proximo = pProximo

  def mostrarNo(self):
    print(f"Valor: {self.__valor}")

#---------------------------------------#

class CabecaDaLista():

  def __init__(self):
    self.__primeiro = None
    self.__ultimo = None

  def __listaVazia(self):
    return self.__primeiro == None

  def inserirNoInicio(self, valor):
    novoNo = No(valor)

    # Se a lista estiver vazia (primeira inserção) o último nó da lista será o nó que acabou de ser criado (apesar de ser uma inserção ao início).
    if self.__listaVazia():
      self.__ultimo = novoNo

    # Do contrário o anterior do primeiro nó recebe a referência de 'novoNo', porque este será o novo 'primeiro'.
    else:
      self.__primeiro.anterior = novoNo

    # O próximo do nó que acaba de ser criado será o que até então era primeiro nó da lista.
    novoNo.proximo = self.__primeiro

    # O primeiro nó da lista encadeada passa a ser o nó recém criado.
    self.__primeiro = novoNo

  def inserirNoFinal(self, valor):
    novoNo = No(valor)

    # Se a lista estiver vazia (primeira inserção) o primeiro nó da lista será o nó que acabou de ser criado (apesar de ser uma inserção ao final).
    if self.__listaVazia():
      self.__primeiro = novoNo

    else:
      self.__ultimo.proximo = novoNo
      novoNo.anterior = self.__ultimo

    self.__ultimo = novoNo

  def mostrarPeloInicio(self):
    if self.__listaVazia():
      print("Erro, lista vazia")
      return None

    atual = self.__primeiro

    print("\nMostrando lista do início para o final:")
    while atual != None:
      atual.mostrarNo()
      atual = atual.proximo

  def mostrarPeloFinal(self):
    if self.__listaVazia():
      print("Erro, lista vazia")
      return None

    atual = self.__ultimo

    print("\nMostrando lista do final para o início:")
    while atual != None:
      atual.mostrarNo()
      atual = atual.anterior

  def pesquisar(self, pValor):

    if self.__listaVazia():
      print("Erro, lista vazia")
      return None

    atual = self.__primeiro

    print(f"\nPesquisando elemento {pValor}")

    while atual.valor != pValor:

      if atual.proximo == None:
        print(f"Elemento não encontrado!")
        return None
      else:
        atual = atual.proximo

    print(f"Elemento encontrado!")
    atual.mostrarNo()
    return atual

  def excluirNoInicio(self):
    if self.__listaVazia():
      print("Erro, lista vazia")

    print("\nExcluindo do início da lista. Elemento excluído:")
    self.__primeiro.mostrarNo()

    itemExcluido = self.__primeiro
    self.__primeiro = self.__primeiro.proximo
    self.__primeiro.anterior = None
    return itemExcluido

  def excluirNoFinal(self):
    if self.__listaVazia():
      print("Erro, lista vazia")

    print("\nExcluindo do final da lista. Elemento excluído:")
    self.__ultimo.mostrarNo()

    itemExcluido = self.__ultimo
    self.__ultimo = self.__ultimo.anterior
    self.__ultimo.proximo = None
    return itemExcluido

  def excluirNaPosicao(self, pValor):
    if self.__listaVazia():
      print("Erro, lista vazia")

    atual = self.__primeiro

    print("\nBuscando elemento para excluir do meio da lista.")

    while atual.valor != pValor:
      if atual.proximo == None:
        print("Elemento não encontrado!")
        return None
      else:
        atual = atual.proximo

    if atual == self.__primeiro:
      return self.excluirNoInicio()
    elif atual == self.__ultimo:
      return self.excluirNoFinal()
    else:
      atual.anterior.proximo = atual.proximo
      atual.proximo.anterior = atual.anterior

    print(f"Elemento encontrado!")
    atual.mostrarNo()
    return atual

#---------------------------------------#

lista = CabecaDaLista()

lista.inserirNoInicio(10)
lista.inserirNoInicio(20)
lista.inserirNoInicio(30)
lista.inserirNoInicio(40)
lista.inserirNoInicio(50)
lista.inserirNoInicio(60)
lista.inserirNoInicio(90)
lista.inserirNoInicio(80)

lista.mostrarPeloInicio()

lista.excluirNoInicio()

lista.mostrarPeloInicio()

itemDaBusca = lista.pesquisar(20)

lista.excluirNaPosicao(40)
lista.excluirNaPosicao(80)

lista.mostrarPeloFinal()
