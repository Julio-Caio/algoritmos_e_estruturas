# Autor: Julio Caio Rodrigues

class QueueException(Exception):
    """
    Uma classe que permite enviar mensagens quando exceções são identificadas na execução daquele código
    """
    def __init__(self, message):
        super().__init__(message)

class Node:
    """
    Representa um nó na fila.

    Atributos:
    carga: O valor armazenado dentro do nó.
    next: Referencia o próximo nó na fila.

    """

    def __init__(self, carga):
        self.__carga = carga
        self.__next = None
    
    def get_item(self):
        """
        Retorna o nó atual
        """
        return self.__carga

    def get_next(self):
        """
        Retorna o nó seguinte ao atual
        """
        return self.__next

    def set_next(self, next_node):
        """
        Atribue um novo valor ao próximo nó
        """
        self.__next = next_node

class Queue:
    """
    Esta classe é uma implementação da estrutura de dados "Fila"
    """
    def __init__(self):
        self.__frente = None
        self.__fundo = None
        self.__tamanho = 0
    
    def __str__(self):
        elements = ""
        atual = self.__frente
        while atual:
            elements += str(atual.get_item())

            if atual.get_next() is not None:
                elements += "-> "
            atual = atual.get_next()
        return "(Front) -> " + elements if elements else "Empty Queue"

    def is_empty(self):
        """
        Verifica se a fila está vazia
        """
        return self.__tamanho == 0

    @property
    def size(self):
        """
        Devolve o tamanho atual da fila (quantidade de elementos)
        """
        return self.__tamanho
    
    def enqueue(self, carga):
        """
        Adiciona um novo nó ao final da fila.

        Parâmetros:
        carga: O valor a ser armazenado no novo nó.

        Se a fila estiver vazia, o novo nó se torna o primeiro e o último elemento.
        Caso contrário, o novo nó é adicionado ao final da fila.
        """
        newNode = Node(carga)

        if self.is_empty():
            self.__frente = newNode
            self.__fundo = newNode
        else:
        # se não, o atributo next presente no último elemento, começa a apontar para este novo
        # após isso, o atributo do útlimo elemento atualiza para o novo valor inserido no final da fila
            self.__fundo.set_next(newNode)
            self.__fundo = newNode

        # após incrementar um novo elemento na fila, atualize o tamanho
        self.__tamanho += 1
    
    def dequeue(self):
        # se a fila estiver vazia, retorne a Exception que definimos
        if self.is_empty():
            raise QueueException(self._get_empty_queue_msg())
        
        # se não, capture o valor do primeiro elemento
        node_removed = self.__frente.get_item()
        # o elemento da frente é agora o valor que vinha logo após a ele na fila anterior
        self.__frente = self.__frente.get_next()
        # decremente o tamanho da fila
        self.__tamanho -= 1

        return node_removed

    def _get_empty_queue_msg(self):
        return "Queue is Empty! Please enqueue an item before dequeuing."

    def print_queue(self):
        if self.is_empty():
            print("Queue is Empty! Nothing to show...")
        else:
            print(f"Queue: {self.__str__()}")

if __name__ == "__main__":
    queue = Queue()

    try:
        queue.dequeue()
    except QueueException as e:
        print(f"Error: {e}")

    for i in range(1, 9):
        queue.enqueue(i)
    
    print(f"Current Queue Size: {queue.size}")
    queue.print_queue()

    for i in range(5):
        try:
            queue.dequeue()
        except QueueException as e:
            print(f"Error: {e}")

    queue.print_queue()