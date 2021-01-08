# Analisando as principais diferenças entre Vetores Ordenados e Não Ordenados

from VetorNaoOrdenado import VetorNaoOrdenado
from VetorOrdenado import VetorOrdenado
import timeit as t
import random 

elementos = []
for _ in range(10000):
    elementos.append(round(random.random(), 4))


# Comparativo de Inserção
def insere_nao_ordenado(lista):
    vetor = VetorNaoOrdenado(len(lista))
    for i in lista:
        vetor.insere(i)
    return vetor

def insere_ordenado(lista):
    vetor = VetorOrdenado(len(lista))
    for i in lista:
        vetor.insere(i)
    return vetor 

# RESOLUÇÃO: A inserção de elementos em um vetor ordenado tem a complexidade O(n)
#            A inserção de elementos em um vetor não ordenado tem a complexidade de O(1)   



# Comparativo de Pesquisa
vetor_nao_ordenado = insere_nao_ordenado(elementos)

# print(len(vetor_nao_ordenado.valores))

vetor_ordenado = insere_ordenado(elementos)
# print(len(vetor_nao_ordenado.valores))

pesquisa = []
for _ in range(10000):
    pesquisa.append(round(random.random(), 4))
print(len(pesquisa))

def pesquisa_nao_ordenado(lista):
    for i in lista:
        vetor_nao_ordenado.pesquisar(i)

def pesquisa_ordenado_binaria(lista):
    for i in lista:
        vetor_ordenado.pesquisa_binaria(i)

# RESOLUÇÃO: Em vetores ordenados a pesquisa é O(log n)
#            Em vetores não ordenados a pesquisa é linear, ou seja, O(n/2) -> O(n)

'''
CONCLUSÃO DOS VETORES ORDENADOS

- A principal vantagem é que os tempos de pesquisa são muito mais rápidos do que em
  um vetor não ordenado

- A inserção leva mais tempo, pois os itens de dados devem ser movidos para criar espaço

- As remoções são lentas tanto nos vetores ordenados quanto nos não ordenados, pois os
  itens devem ser movidos para preencher o "buraco"

- Vetores ordenados são úteis quando pesquisas são frequentes, mas inserções e remoções
  não são

Qual o tipo de vetor mais adequado para
    
    * Um cadastro de funcionários? Vetor não ordenado
    * Um cadastro de produtos de uma loja de varejo? Vetor ordenado
'''

