# Autor: Julio Caio Rodrigues

# Data: 26/10/2024

"""
Implementação da estrutura de dados Fila
"""

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
        """Retorna o valor armazenado no nó."""

        return self.__carga

    @property
    def next(self):
        return self.__next

    @next.setter
    def next(self, next_node):
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
            atual = atual.next  # Usando o atributo next diretamente
            if atual is not None:
                elements += "-> "
        return "(Front) -> " + elements if elements else "Empty Queue"

    def is_empty(self):
        """Verifica se a fila está vazia."""

        return self.__tamanho == 0

    @property
    def tamanho(self):
        """Devolve o tamanho atual da fila (quantidade de elementos)."""

        return self.__tamanho
    
    def enqueue(self, elemento):
        """Adiciona um novo nó ao final da fila."""

        if elemento is None:
            raise QueueException("Não é permitido inserir um valor None na fila.")

        new_node = Node(elemento)

        if self.is_empty():
            self.__frente = new_node
            self.__fundo = new_node
        else:
            self.__fundo.next = new_node
            self.__fundo = new_node

        self.__tamanho += 1
    
    def dequeue(self):
        """Remove e retorna o primeiro elemento da fila."""
        if self.is_empty():
            raise QueueException(self._get_empty_queue_msg())
        
        node_removed = self.__frente.get_item()
        self.__frente = self.__frente.next
        self.__tamanho -= 1

        return node_removed
    
    def peek(self):
        """Devolve o primeiro elemento sem removê-lo."""
        if self.is_empty():
            raise QueueException(self._get_empty_queue_msg())
        return self.__frente.get_item()
    
    def clear(self):
        """Esvazia a fila liberando cada um dos nós."""
        while self.__frente is not None:
            tmp = self.__frente
            self.__frente = self.__frente.next
        
        self.__fundo = None
        self.__tamanho = 0

    def _get_empty_queue_msg(self):
        return "Queue is Empty! Please enqueue an item before dequeuing.\n"

    def print_queue(self):
        if self.is_empty():
            print(self._get_empty_queue_msg())
        else:
            print(f"Queue: {self.__str__()}")

if __name__ == "__main__":
    queue = Queue()
    
    # Tentar remover um elemento de uma fila vazia
    try:
        queue.dequeue()
    except QueueException as e:
        print(f"\nError: {e}\n")

    print("Adicionando elementos (1-8)...\n")
    for i in range(1, 9):
        queue.enqueue(i)
    
    print(f"Current Queue Size: {queue.tamanho}\n")
    queue.print_queue()

    # Desenfileirar 5 elementos
    for _ in range(5):
        try:
            queue.dequeue()
        except QueueException as e:
            print(f"Error: {e}")

    queue.print_queue()

    print("\nLimpando a fila...")
    queue.clear()
    print()
    queue.print_queue()