

class VetorOrdenado():
    '''Classe de vetores ordenados - Insira o tamanho do vetor ao instanciar a classe'''
    def __init__(self, capacidade):
        import numpy as np
        self.capacidade = capacidade 
        self.ultima_posicao = -1 
        self.valores = np.empty(self.capacidade, dtype=float)

    # O(n)
    def imprime(self):
        if self.ultima_posicao == -1:
            print('O vetor está vazio')
        else:
            for i in range(self.ultima_posicao + 1):
                print(f'{i} - {self.valores[i]}')

    # O(n)
    def insere(self, valor):
        if self.ultima_posicao == self.capacidade - 1:
            print('Capacidade máxima atingida')
            return
        
        posicao = 0 
        for i in range(self.ultima_posicao + 1):
            posicao = i
            if self.valores[i] > valor:
                break
            if i == self.ultima_posicao:
                posicao = i + 1

        x = self.ultima_posicao
        while x >= posicao: 
            self.valores[x+1] = self.valores[x]
            x -= 1 

        self.valores[posicao] = valor 
        self.ultima_posicao += 1
    
    # O(n)
    def pesquisa_linear(self, valor):
        for i in range(self.ultima_posicao + 1):
            if self.valores[i] > valor:
                return -1 
            if self.valores[i] == valor: 
                return i 
            if i == self.ultima_posicao:
                return -1

    # O(log n)
    def pesquisa_binaria(self, valor):
        limite_inferior = 0
        limite_superior = self.ultima_posicao

        while True:
            posicao_atual = (limite_inferior + limite_superior) // 2
            # se achou na primeira tentativa
            if self.valores[posicao_atual] == valor:
                return posicao_atual
            # se nao achou
            elif limite_inferior > limite_superior:
                return -1 
            # Divide os limites
            else:
                # Limite inferior
                if self.valores[posicao_atual] < valor:
                    limite_inferior = posicao_atual + 1
                # Limite superior
                else:
                    limite_superior = posicao_atual - 1

    # O(n)
    def excluir(self, valor):
        posicao = self.pesquisa_linear(valor)
        if posicao == -1: 
            return -1 
        else:
            for i in range(posicao, self.ultima_posicao):
                self.valores[i] = self.valores[i+1]

            self.ultima_posicao -= 1


if __name__ == "__main__":    

    vetor = VetorOrdenado(10)
    '''
    vetor.insere(6)
    vetor.insere(4)    
    vetor.insere(3)
    vetor.insere(5)
    vetor.insere(1)
    vetor.insere(8)

    vetor.pesquisar(3)
    vetor.pesquisar(2)
    vetor.pesquisar(9)

    vetor.excluir(5)
    vetor.excluir(9)
    '''

    
    vetor.insere(8)
    vetor.insere(9)
    vetor.insere(4)
    vetor.insere(1)
    vetor.insere(5)
    vetor.insere(7)
    vetor.insere(11)
    vetor.insere(13)
    vetor.insere(2)
    vetor.imprime()

    print(vetor.pesquisa_binaria(7))
    print(vetor.pesquisa_binaria(5))
    print(vetor.pesquisa_binaria(13))
    print(vetor.pesquisa_binaria(20))
    

   