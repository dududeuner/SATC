import numpy as np

class Pilha():
    def __init__(self, pCapacidade):
        self.__capacidade = pCapacidade
        self.__topo = -1
        self.valores = np.empty(pCapacidade, dtype=int)

    def empilhar(self, valor):
        if self.__topo == self.__capacidade -1:
            print('Erro, Pilha esta cheia')
        else:
            self.__topo += 1
            self.valores[self.__topo] = valor
            #print(self.valores[self.__topo])
            #print(self.valores)

    def desempilhar(self):
        if self.__topo == -1:
            print('Erro, Pilha esta vazia')
        else:
            self.valores[self.__topo] = 0
            #print(self.__topo)
            #print(self.valores[self.__topo])
            #print(self.valores)

    def verTopo(self):
        if self.__topo != -1:
            print(self.valores[self.__topo])
        else:
            print('a fila esta vazia')




pilha = Pilha(8)

pilha.empilhar(10)
pilha.empilhar(20)
pilha.empilhar(30)
pilha.empilhar(40)
pilha.empilhar(50)
pilha.empilhar(60)



pilha.verTopo()

pilha.desempilhar()

pilha.verTopo()




