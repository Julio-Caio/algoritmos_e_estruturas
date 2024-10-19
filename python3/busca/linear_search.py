from time import time

class LinearSearch:
    def __init__(self, array: list, item: any):
        self.array = array
        self.item = item
        self.__totalOperations = 0

    def __search(self):
        """
        Método privado que realiza a busca linear.

        Percorre todos os elementos do array até encontrar o item.

        Retorna:
        - O índice do item no array, caso encontrado.
        - None, caso o item não esteja presente.
        """
        for index, current in enumerate(self.array):
            self.__totalOperations += 1 

            if current == self.item:
                return index

        return None

    def search(self):
        start_time_exec = time()
        position = self.__search()
        end_time_exec = time()
        execution_time = end_time_exec - start_time_exec
        print(f"Total Operations: {self.__totalOperations}")
        return execution_time, self.__totalOperations