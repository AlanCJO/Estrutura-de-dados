import numpy as np
import sys

class PilhaDelimitadora:
    """
        capacidade apenas com valor par\n
        valores apenas char
    """
    def __init__(self, capacidade):
        if capacidade % 2 != 0:
            sys.exit()
        self.__capacidade = capacidade         
        self.__topo = -1
        self.__valores = np.empty(self.__capacidade, dtype=str)
        print('oi')


pilha = PilhaDelimitadora(3)