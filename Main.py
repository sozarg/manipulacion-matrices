def incializar_matriz(cantidad_filas:int, cantidad_columnas:int, valor_inicial:any) -> list:
    matriz = []
    for i in range(cantidad_filas):
        filas = [valor_inicial] * cantidad_columnas
        matriz += [filas]
    return matriz

def mostrar_matriz(matriz:list) -> None:
    for i in range(len(matriz)):
        for j in range(len(matriz[i])):
            print(matriz[i][j], end= "\t")
        print()

