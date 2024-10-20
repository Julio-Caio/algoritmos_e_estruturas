# Autor: Julio Caio Rodrigues

"""
Parte dos meus estudos em Estrutura de Dados e Algoritmos

Fibonacci - Versão Recursiva
"""

def fib(n: int) -> int:
    """
    Função recursiva para calcular o n-ésimo número de Fibonacci.

    A sequência de Fibonacci é definida como:
    fib(n) = fib(n-1) + fib(n-2) para n > 1
    fib(0) = 0
    fib(1) = 1

    Para fib(n), onde n é 10, considere:
        fib(10) = fib(9) + fib(8)
                 = (fib(8) + fib(7)) + (fib(7) + fib(6))
                 = ...
        Resultado final para fib(10) é 55.
    """

    # Caso base: se n é 0 ou 1, retorna n
    if n <= 1:
        return n

    return fib(n - 1) + fib(n - 2)

def seq_fib(n: int, lista: list=None, index: int=0)-> list:
    
    if lista is None:
        lista = []
    
    if index >= n:
        return lista

    lista.append(fib(index))

    return seq_fib(n, lista, index + 1)


if __name__ == "__main__":
    n = 10
    resultado = fib(n)
    print(f"O {n}-ésimo número de Fibonacci é: {resultado}")

    sequencia_fib = seq_fib(n)
    print(f"A sequência de Fibonacci até o {n}-ésimo número é: {sequencia_fib}")

    # Demonstração do fluxo da chamada
    """
    O fluxo de chamadas pode ser visualizado assim:
    
    fib(5) = fib(4) + fib(3)
           = (fib(3) + fib(2)) + (fib(2) + fib(1))
           = ((fib(2) + fib(1)) + 1) + (1 + 0)
           = (2 + 1) + 1
           = 5
           
    Onde:
    - fib(2) = fib(1) + fib(0) = 1 + 0 = 1
    - fib(1) = 1
    - fib(0) = 0
    """