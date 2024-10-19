# Autor:     Julio Caio Rodrigues

"""
    Isto faz parte dos meus estudos em Estrutura de Dados e Algoritmos

    Notação Big O da pesquisa binária:
        log N, sendo que, para uma lista de N elementos, o número total de buscas corresponde ao log de seu N elementos
"""

from time import time

class BinarySearch:
    """
    Classe para realizar a busca binária em um array ordenado.
    
    Atributos:
    - array: Lista de elementos onde a busca será realizada.
    - item: Elemento a ser buscado no array.
    - __totalOperations: Contador do número de operações realizadas.
    - __length: Índice do limite superior do array.
    - __smaller: Índice do limite inferior do array.
    """
    
    def __init__(self, array: list, item: any):
        """
        Inicializa a classe BinarySearch com o array e o item a ser buscado.

        Parâmetros:
        - array: Lista ordenada de elementos.
        - item: Valor a ser encontrado no array.
        """
        self.array = array
        self.item = item
        self.__totalOperations = 0
        self.__length = len(self.array) - 1
        self.__smaller = 0

    def __search(self):
        """
        Método privado que realiza a busca binária.

        O array é dividido repetidamente pela metade até que o item seja encontrado
        ou que os limites inferior e superior se cruzem, indicando que o item não
        está presente no array.

        Retorna:
        - O índice do item no array, caso encontrado.
        - None, caso o item não esteja presente.
        """
        while self.__smaller <= self.__length:
            middle_pos = (self.__smaller + self.__length) // 2
            current = self.array[middle_pos]

            self.__totalOperations += 1

            print(f"""\nStep {self.__totalOperations}: 
            Current part of array being searched:
            {self.array[self.__smaller:self.__length + 1]}\n""")

            if current > self.item:
                self.__length = middle_pos - 1

            elif current < self.item:
                self.__smaller = middle_pos + 1

            else:
                return middle_pos
        return None

    def print_position(self):
        """
        Imprime a posição do item no array, ou uma mensagem indicando que
        o item não foi encontrado.
        """

        start_time_exec = time()
        position = self.__search()

        if position is not None:
            print(f"\nPosition of {self.item} in the array is {position}")
        else:
            print(f"\n{self.item} not found in the array")

        end_time_exec = time()

        total_execution_time = end_time_exec - start_time_exec
        print(f"Execution Time: {total_execution_time:.6f} seconds")


def get_integer_input():
    """Função para obter um número inteiro do usuário com validação."""
    while True:
        try:
            user_input = int(input("\nType a number that you wish to know its position in the array: "))
            return user_input
        except ValueError:
            print("Invalid value. Please enter a valid integer.")

if __name__ == "__main__":
    lista_ex1 = [0, 1, 2, 3, 4, 5, 6, 7, 8]
    lista_ex2 = [1, 3, 5, 7, 9, 11, 13, 15]

    item = get_integer_input()

    binarySearch = BinarySearch(lista_ex1, item)
    binarySearch.print_position()

    binarySearch = BinarySearch(lista_ex2, item)
    binarySearch.print_position()