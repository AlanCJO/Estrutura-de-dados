import numpy as np
import sys

class PilhaDelimitadora:
    """
        capacidade apenas com valor par\n
        valores apenas char
    """
    def __init__(self, capacidade):
        # capacidade par
        if capacidade % 2 != 0:
            print("Capacidade ímpar!")
            sys.exit()

        self.__capacidade = capacidade         
        self.__topo = -1
        self.__valores = np.empty(self.__capacidade, dtype=str)

    def __pilha_cheia(self):
        if self.__topo == self.__capacidade - 1:
            return True
        else:
            return False

    def __pilha_vazia(self):
        if self.__topo == -1:
            return True
        else:
            return False

    def empilhar(self, valor:str):
        """
            somente tipo char
        """
        if type(valor) == int or type(valor) == float:
            print("Tipo de entrada inválido!")
            sys.exit()
        if len(valor) != 1:
            print("Apenas tipo char!")
            sys.exit() 


pilha = PilhaDelimitadora(4)
pilha.empilhar('21')