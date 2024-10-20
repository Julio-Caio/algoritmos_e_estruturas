from fatorial import fatorial

def fatorialLista(arr: list, seq_fat: list=None, index:int=0) -> list:
    if arr is None:
        return -1
    
    if seq_fat is None:
        seq_fat = []
    
    if index >= len(arr):
        return seq_fat

    seq_fat.append(fatorial(arr[index]))

    return fatorialLista(arr, seq_fat, index + 1)
    
if __name__ == "__main__":
    array1 = [3,4,5,6,8,10]
    lista_fatoriais = fatorialLista(array1)
    print(lista_fatoriais)