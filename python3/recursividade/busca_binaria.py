# Autor: Julio Caio Rodrigues

"""
Parte dos meus estudos em Estrutura de Dados e Algoritmos

Busca Binária - Versão Recursiva
"""

def binarySearch(array: list, item: int, index_low: int, index_high: int) -> int:
    """
    Implementação recursiva da busca binária:
    1. Determine o índice mais baixo (index_low) e o mais alto (index_high).
    2. Calcule o índice do meio: index_middle = (index_low + index_high) // 2.
    3. Compare o item do meio com o item procurado:
        a. Se for igual, retorna o índice.
        b. Se o item do meio for maior, repete a busca à esquerda.
        c. Se o item do meio for menor, repete a busca à direita.
    4. Retorna -1 se o item não for encontrado.
    """
    # Caso base: se os índices se cruzam, o item não está no array
    if index_low > index_high:
        return -1

    # Calculamos o índice do meio
    index_middle = (index_low + index_high) // 2

    # Verificamos se o item do meio é o item buscado
    if array[index_middle] == item:
        return index_middle
    # Se o item do meio é maior, busca na metade esquerda
    elif array[index_middle] > item:
        return binarySearch(array, item, index_low, index_middle - 1)
    # Se o item do meio é menor, busca na metade direita
    else:
        return binarySearch(array, item, index_middle + 1, index_high)


if __name__ == '__main__':
    arr = [2, 3, 4, 10, 12, 24, 26, 40, 65, 88]
    item = 10
    
    result = binarySearch(arr, item, 0, len(arr)-1)
    
    if result != -1:
        print(f"\nElemento está presente no array, no índice: {result}")
    else:
        print("\nElemento não está presente no array!")