def invertString(string:str, indice:int=0) -> str:
    # caso base
    if indice == len(string):
        return ""

    # caso recursivo
    return invertString(string, indice + 1) + string[indice]

print(invertString("egnaugnal retteb si nohtyp"))