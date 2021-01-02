'''
Funções Big-O 

* 1 Constant
* log(n) Logarithmic
* n Linear
* nlog(n) Log Linear
* n^2 Quadratic
* n^3 Cubic
* 2^n Exponetial
'''

from math import log 
import numpy as np 
import matplotlib.pyplot as plt 

n = np.linspace(1, 10, 100)

labels = ['Constant', 'Logarithmic', 'Linear', 'Log linear', 'Quadratic', 'Cubic', 'Exponential']
big_o = [np.ones(n.shape), np.log(n), n, n * np.log(n), n**2, n**3, 2**n]

plt.figure(figsize=(10,8))
plt.ylim(0, 100)

for i in range(len(big_o)):
    plt.plot(n, big_o[i], label = labels[i])
plt.legend()
plt.ylabel('Runtime')
plt.xlabel('n')
plt.title("Complexido de Tempo das funções Big O")
plt.show()