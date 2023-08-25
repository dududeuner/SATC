#vetores ordenados
import numpy as np


class exemplo():
    def __init__(self, pCapacidade):
        self.__capacidade = pCapacidade
        self.__ultima_posicao = -1
        self.__valores = np.empty(pCapacidade, dtype=int)

    def inserir(self, valor):
        if self.__capacidade == self.__ultima_posicao + 1:
            print('O vetor esta cheio')
        elif self.__ultima_posicao == -1:
            print(f'vetor vazio. Inserindo elemento {valor} na primeira posição')
            self.__ultima_posicao += 1
            self.__valores[self.__ultima_posicao] = valor
        else:
            posicao = 0
# Encontrar a posição
            print(f'buscando posição para inserir elemento {valor}')
            for i in range(0, self.__ultima_posicao + 1):
                
                posicao = i

                if self.__valores[i] > valor:
                    print(f'Posicao encontrada : {i}')
                    break
                elif i == self.__ultima_posicao:
                    posicao = i + 1
# Deslocar os elementos posteriores para frente
            x = self.__ultima_posicao

            while x >= posicao:
                print(f"Deslocando o elemento {self.__valores[x]} para a posição {x + 1}")
                self.__valores[x + 1] = self.__valores[x]
                x -= 1
            print(f'Inserindo elemento {valor} na posição {posicao}')
            self.__valores[posicao] = valor
            self.__ultima_posicao += 1

    def imprimir(self):
        for i in range(0, self.__ultima_posicao + 1):
            print(f'valor na posicao {i} : {self.__valores[i]}')



vetor = exemplo(10)



vetor.inserir(1)
vetor.inserir(2)
vetor.inserir(4)
vetor.inserir(5)
vetor.inserir(6)
vetor.inserir(3)

vetor.imprimir()