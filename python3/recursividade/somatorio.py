def somatorio_simples(array: list):
    """
    Função recursiva simples para calcular o somatório de uma lista.
    """
    ## Caso base: se o array for vazio, retorna 0 ##
    if len(array) == 0:
        return 0

    print(f'\n[ + ] Somando {array[0]} com somatorio({array[1:]})\n')

    ## Caso recursivo: somamos o primeiro elemento com o somatório do restante ##
    return array[0] + somatorio_simples(array[1:])

def somatorio_com_indices(array: list, indice = 0):
    """
    Função recursiva usando índices para calcular o somatório de uma lista.
    """
    ## Caso base: se o índice for o último, retorna o valor nesse índice ##
    if indice == len(array) - 1:
        return array[indice]

    print(f'\n[ + ] Somando {array[indice]} com somatorio_com_indices(array, indice + 1)\n')

    ## Chamada recursiva: soma o elemento atual com o próximo ##
    return array[indice] + somatorio_com_indices(array, indice + 1)

if __name__ == "__main__":
    array1 = [1, 3, 5, 7]
    array2 = [2, 4, 6, 8]

    operacao1 = somatorio_com_indices(array1, 0)
    operacao2 = somatorio_simples(array1)

    print("Somatório usando índices:", operacao1)
    print("Somatório simples e direto:", operacao2)