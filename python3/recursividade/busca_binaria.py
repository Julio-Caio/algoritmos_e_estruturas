# Autor:     Julio Caio Rodrigues

"""
    Isto faz parte dos meus estudos em Estrutura de Dados e Algoritmos

    Busca Binária Versão Recursiva
"""

def binarySearch(array: list, item: int, index_low, index_high):
    """
    a Busca Binária consiste em:
    1) Determine o indice do elemento mais baixo da lista = 0
    2) Determine o indice do último elemento da lista = len(array) - 1
    3) Após isso, some os dois indices e determine o indice do meio = (i_low + i_last) // 2
    4) Após isso, verifique na lista, o elemento que possui esse indice, e a partir disso, verifique:
        4.1) ele é o elemento que procuro? (item == array[indice_meio])
        4.2) ele é maior do que procuro?
            4.2.1 - se sim, divida a lista novamente em duas e pegue a parte a esquerda -> indice_meio - 1
        4.3) ele é menor do que procuro?
             indice_meio + 1
        4.4 se não encontrar None
    """
    index_middle = (index_low + index_high) // 2
    # caso base
    if index_low >= index_high:
        return index_low + (index_high - index_low) // 2

    elif array[index_middle] == item:
        return index_middle

    elif array[index_middle] > item:
         return binarySearch(array, item, index_low, index_middle - 1)

    elif array[index_middle] < item:
        return binarySearch(array, item, index_middle + 1, index_high)

    else:
        return -1

    
if __name__ == '__main__':
    arr = [2, 3, 4, 10, 12, 24, 26, 40, 65, 88]
    item = 10
    
    result = binarySearch(arr, 10, 0, len(arr)-1)
    
    if result != -1:
        print("\nElemento está presente no array, no indíce: ", result)
    else:
        print("\nElemento Não está presente no array!")