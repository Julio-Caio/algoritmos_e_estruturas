'''
Exemplo de fatorial:
    !6 = 6 * 5 * 4 * 3 * 2 * 1

Caso base:
    Quando o número for igual a 0, encerre a execução.
'''

def fatorial(n: int):
    """
    Função recursiva para calcular o fatorial de um número.
    """
    ## Caso base: se o número for 0, retorna 1 ##
    if n == 0:
        return 1
    ## Chamada recursiva: n * fatorial(n - 1) ##
    return n * fatorial(n - 1)

'''
Pilha de chamadas:

return n * fatorial(n - 1)

6 * (6 - 1)   --> 5 * (5 - 1)   --> 4 * (4 - 1) --> ( 3 - 1) --> (2 - 1) --> 1 - 1 --> 0 -> atingimos o caso base
      5           4                 3                   2           1 
'''
if __name__ == "__main__":
    print(fatorial(6))  # Saída esperada: 720
    print(fatorial(3))  # Saída esperada: 6
    print(fatorial(9))  # Saída esperada: 362880