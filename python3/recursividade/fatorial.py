'''
Exemplo de fatorial:
    !6 = 6 * 5 * 4 * 3 * 2 * 1

Caso base:
    Quando o número for igual a 0, retorne 1.
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

if __name__ == "__main__":
    print(fatorial(6))  # Saída esperada: 720
    print(fatorial(3))  # Saída esperada: 6
    print(fatorial(9))  # Saída esperada: 362880