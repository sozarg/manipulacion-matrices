def incializar_matriz(cantidad_filas:int, cantidad_columnas:int, valor_inicial:any) -> list:
    matriz = []
    for i in range(cantidad_filas):
        filas = [valor_inicial] * cantidad_columnas
        matriz += [filas]
    return matriz

