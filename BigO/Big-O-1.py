# https://colab.research.google.com/drive/1B4kcOEG5iDkT8N07NjPnOOXXWcp6VfZo?usp=sharing
# https://wiki.python.org/moin/TimeComplexity

import timeit

# Função 1 - O(n)
time_in_seconds = timeit.timeit("soma1(10)", 
'''def soma1(n):
    soma = 0; 
    for i in range(n + 1): 
        soma += i; return soma''', number=1000)

print(f'\nEficiência da função 1 em segundos: {time_in_seconds}')

# Função 2 - O(3)
time_in_seconds = timeit.timeit("soma2(10)", '''
def soma2(n):
    return(n * (n + 1)) / 2
''', number = 1000)

print(f'Eficiência da função 2 em segundos: {time_in_seconds}\n')