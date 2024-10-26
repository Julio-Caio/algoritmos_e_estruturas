# Autor: Julio Caio Rodrigues

# Data: 26/10/2024

"""
Implementação da estrutura de dados Pilha
"""

class StackException(Exception):
    """
    Uma classe que permite enviar mensagens quando exceções são identificadas na execução daquele código
    """
    def __init__(self, mesg):
        super().__init__(mesg)


class Node:
    """
    Representa um nó na pilha.

    Atributos:
    carga: O valor armazenado dentro do nó.
    next: Referencia o próximo nó na pilha.
    """
    def __init__(self, carga):
        self.__carga = carga
        self.__next = None

    @property
    def carga(self):
        """Retorna o valor armazenado no nó."""
        return self.__carga

    @property
    def next(self):
        """Retorna o próximo nó."""
        return self.__next

    @next.setter
    def next(self, next_node):
        """Atribui um novo nó como próximo."""
        self.__next = next_node


class Stack:
    def __init__(self):
        self.__tamanho = 0
        self.__topo = None

    def push(self, elemento):
        """
        Método para adicionar um elemento ao topo da pilha.
        """
        if elemento is None:
            raise StackException("Não é permitido inserir um valor None na pilha.")

        novo_no = Node(elemento)
        novo_no.next = self.__topo
        self.__topo = novo_no 
        self.__tamanho += 1

    def _get_empty_stack_msg(self):
        """Mensagem para pilha vazia."""
        return "Pilha vazia, não há nada para retornar..."

    def pop(self):
        """
        Método para remover e retornar o elemento do topo da pilha.
        """
        if self.is_empty():
            raise StackException(self._get_empty_stack_msg())
        
        elemento_removido = self.__topo.carga
        self.__topo = self.__topo.next
        self.__tamanho -= 1
        return elemento_removido

    def peek(self):
        """
        Retorna o valor do topo da pilha, sem remoção.
        """
        if self.is_empty():
            raise StackException(self._get_empty_stack_msg())

        return self.__topo.carga

    def is_empty(self):
        """
        Verifica se a pilha está vazia.
        """
        return self.__topo is None

    @property
    def tamanho(self):
        """Retorna o número de elementos na pilha."""
        return self.__tamanho

    def __str__(self):
        pilha = ""
        atual = self.__topo

        while atual:
            pilha += str(atual.carga)
            
            if atual.next is not None:
                pilha += "-> "
            
            atual = atual.next
        return "Topo -> " + pilha

    def clear(self):
        self.__topo = None

    def imprimir_pilha(self):
        print(f"Pilha: {self.__str__()}")

if __name__ == "__main__":
    pilha = Stack()

    # Adicionar os elementos de 1 a 9 à pilha
    for i in range(1, 10):
        pilha.push(i)
    
    pilha.imprimir_pilha()

    # Remove 3 elementos do topo da pilha
    for _ in range(3):
        pilha.pop()
    
    pilha.imprimir_pilha()

    # Tenta adicionar None à pilha
    try:
        pilha.push(None)
    except StackException as e:
        print(f"\nError: {e}")

    print("\nLimpando a fila...")
    pilha.clear()
    pilha.imprimir_pilha()