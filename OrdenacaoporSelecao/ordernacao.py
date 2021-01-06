

class OrdenacaoSelecao:

    def __buscaMenor(self, arr):
        menor = arr[0]
        menor_indice = 0

        for i in range(1, len(arr)):
            if arr[i] < menor:
                menor = arr[i]
                menor_indice = i 
        return menor_indice 

    def selecao(self, arr):
        novoArr = []
        for i in range(len(arr)):
            menor = self._OrdenacaoSelecao__buscaMenor(arr)
            novoArr.append(arr.pop(menor))
        return novoArr
    


lista = [2, 10, 1, 34, 21, 24, 0]

order = OrdenacaoSelecao()
print(order.selecao(lista))