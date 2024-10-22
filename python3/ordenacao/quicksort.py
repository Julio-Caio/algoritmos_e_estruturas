# Autor: Julio Caio Rodrigues

"""
Parte dos meus estudos em Estrutura de Dados e Algoritmos

Ordenação - QuickSort (Dividir P/ Conquistar + Recursividade)
"""

def quicksort(arr):
    if len(arr) <= 1:
        return arr

    pivot = arr[0]
    
    menores = []
    maiores = []

    for item in arr[1:]:
        if item < pivot:
            menores.append(item)
        else:
            maiores.append(item)
    
    return quicksort(menores) + [pivot] + quicksort(maiores)

if __name__ == "__main__":
    array = [5, 2, 1, 4, 9, 7, 3, 6]
    print(f"Resultado: {quicksort(array)}")