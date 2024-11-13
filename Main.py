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

def carga_secuencial(matriz:list) -> list:
    for i in range(len(matriz)):
        for j in range(len(matriz[i])):
            matriz[i][j] += int(input(f"Ingrese el elemento para la fila ({i}) | colummna ({j}): "))

matriz = incializar_matriz(3,3,0)
carga_secuencial(matriz)
mostrar_matriz(matriz)