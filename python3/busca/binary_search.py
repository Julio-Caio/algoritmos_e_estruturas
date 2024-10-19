from time import time

class BinarySearch:
    def __init__(self, array: list, item: any):
        self.array = array
        self.item = item
        self.__totalOperations = 0
        self.__length = len(self.array) - 1
        self.__low = 0

    def __search(self):
        while self.__low <= self.__length:
            middle_pos = (self.__low + self.__length) // 2
            current = self.array[middle_pos]
            self.__totalOperations += 1

            if current > self.item:
                self.__length = middle_pos - 1
            elif current < self.item:
                self.__low = middle_pos + 1
            else:
                return middle_pos

        return None

    def search(self):
        start_time_exec = time()
        position = self.__search()
        end_time_exec = time()
        execution_time = end_time_exec - start_time_exec
        print(f"Total Operations: {self.__totalOperations}")
        return execution_time, self.__totalOperations