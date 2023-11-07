import numpy as np

class Fila():
    def __init__(self, capacidade):
        self.__capacidade = capacidade
        self.__inicio = 0
        self.__fim = -1
        self.__tamanho = 0
        self.valores = np.empty(capacidade, dtype=int)

    def enfileirar(self, valor):
        if not self.esta_cheia():
            self.__fim = (self.__fim + 1) % self.__capacidade
            self.valores[self.__fim] = valor
            self.__tamanho += 1
        else:
            print('Erro, a fila está cheia')

    def desenfileirar(self):
        if not self.esta_vazia():
            valor_desenfileirado = self.valores[self.__inicio]
            self.valores[self.__inicio] = 0  # Limpa o valor na posição
            self.__inicio = (self.__inicio + 1) % self.__capacidade
            self.__tamanho -= 1
            return valor_desenfileirado
        else:
            print('Erro, a fila está vazia')

    def ver_inicio(self):
        if not self.esta_vazia():
            return self.valores[self.__inicio]
        else:
            print('A fila está vazia')

    def esta_cheia(self):
        return self.__tamanho == self.__capacidade

    def esta_vazia(self):
        return self.__tamanho == 0

    def tamanho(self):
        return self.__tamanho

# Exemplo de uso da fila
fila = Fila(8)

fila.enfileirar(10)
fila.enfileirar(20)
fila.enfileirar(30)
fila.enfileirar(40)
fila.enfileirar(50)
fila.enfileirar(60)

print("Elemento no início da fila:", fila.ver_inicio())

fila.desenfileirar()
print("Elemento no início da fila após desenfileirar:", fila.ver_inicio())
