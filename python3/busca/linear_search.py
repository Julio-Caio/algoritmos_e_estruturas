# Autor:     Julio Caio Rodrigues

"""
    Isto faz parte dos meus estudos em Estrutura de Dados e Algoritmos

    Notação Big O da busca linear:
        O(N), onde N é o número de elementos na lista.
"""

from time import time

class LinearSearch:
    """
    Classe para realizar a busca linear em um array.
    
    Atributos:
    - array: Lista de elementos onde a busca será realizada.
    - item: Elemento a ser buscado no array.
    - __totalOperations: Contador do número de operações realizadas.
    """
    
    def __init__(self, array: list, item: any):
        """
        Inicializa a classe LinearSearch com o array e o item a ser buscado.

        Parâmetros:
        - array: Lista de elementos.
        - item: Valor a ser encontrado no array.
        """
        self.array = array
        self.item = item
        self.__totalOperations = 0

    def __search(self):
        """
        Método privado que realiza a busca linear.

        A busca verifica cada elemento do array até encontrar o item
        ou até que todos os elementos tenham sido verificados.

        Retorna:
        - O índice do item no array, caso encontrado.
        - None, caso o item não esteja presente.
        """
        for index, current in enumerate(self.array):
            self.__totalOperations += 1
            
            print(f"\nStep {self.__totalOperations}: Checking element {current}")

            if current == self.item:
                return index  # Retorna o índice se o item for encontrado
        return None  # Retorna None se o item não for encontrado

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

    linearSearch = LinearSearch(lista_ex1, item)
    linearSearch.print_position()

    linearSearch = LinearSearch(lista_ex2, item)
    linearSearch.print_position()