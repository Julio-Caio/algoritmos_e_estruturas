'''
Empilhando:

4231 // 10 = 432
432 // 10 = 43
43 // 10 = 4
4 // 10 = 0

Subindo a pilha:

return 0

4 % 10 = 4
3 % 10 = 3
2 % 10 = 2
1 % 10 = 1

'''

def somatorio_digitos(n) -> int:
    # caso base
    if n == 0:
        return 0

    return somatorio_digitos(n // 10) + n % 10

print(somatorio_digitos(4321))
print(somatorio_digitos(5402))