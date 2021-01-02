print('\n-=-=-=--=-=-=-=-=-==-=-=-=-=-=-=-=-=-=-=')

import timeit as t
# Definindo a eficiência do algoritmo 1

# O(1000) -> O(n)
def lista1():
    lista = []
    for i in range(1000):
        # lista.append(i)
        lista += [i]
    return lista

seconds = t.timeit("lista1()", '''
def lista1():
    lista = []
    for i in range(1000):
        lista += [i]
    return lista''',
number=1000)

print(seconds)

def lista2():
    return range(1000)

seconds2 = t.timeit("lista2()", '''
def lista2():
    return range(1000)''',
number=1000)
print(seconds2)


print('\n-=-=-=--=-=-=-=-=-==-=-=-=-=-=-=-=-=-=-=')