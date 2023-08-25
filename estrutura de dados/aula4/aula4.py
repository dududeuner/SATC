#vetores nao ordenados
import numpy as np


class aula4():
    def __init__(self, pCapacidade):
        self.__capacidade = pCapacidade
        self.__ultima_posicao = -1
        self.__valores = np.empty(pCapacidade, dtype=int)

    def inserir(self, valor):
        if self.__capacidade == self.__ultima_posicao -1:
            print('O vetor esta cheio')
        else:
            self.__ultima_posicao += 1
            self.__valores[self.__ultima_posicao] = valor

    def imprimir(self):
        for i in range(0, self.__ultima_posicao + 1):
            print(f'valor na posicao {i} : {self.__valores[i]}')










vetor = aula4(10)



vetor.inserir(1)
vetor.inserir(2)
vetor.inserir(4)
vetor.inserir(5)
vetor.inserir(6)
vetor.inserir(3)

vetor.imprimir()
