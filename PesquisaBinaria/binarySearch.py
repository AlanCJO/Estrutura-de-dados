# Complexidade de tempo - O(log n) 

def pesquisa_binaria(lista, valor):
    limite_inferior = 0
    limite_superior = len(lista)

    while True:
        posicao_atual = (limite_inferior + limite_superior) // 2

        # se achou na primeira tentativa
        if lista[posicao_atual] == valor:
            return posicao_atual 
        # se não achou
        elif limite_inferior > limite_superior:
            return -1 
        # Divide os limites
        else:
            # Limite inferior
            if lista[posicao_atual] < valor:
                limite_inferior = posicao_atual + 1
            # Limite superior
            else:
                limite_superior - 1