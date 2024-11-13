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

def carga_secuencial(matriz:list) -> None:
    for i in range(len(matriz)):
        for j in range(len(matriz[i])):
            matriz[i][j] += int(input(f"Ingrese el elemento para la fila ({i}) | colummna ({j}): "))

def carga_aleatoria(matriz:list, cantidad_filas:int, cantidad_columnas:int) -> None:
    seguir = "s"
    while seguir == "s":
        fila = int(input("Ingrese la posicion de la fila: "))
        columna = int(input("Ingrese la posición de la columna: "))

        while not validar_carga_aleatoria(fila, columna, cantidad_filas, cantidad_columnas):
            print("Posicion/es ingresada/s fuera de rango. Intente nuevamente")
            fila = int(input("Ingrese la posicion de la fila: "))
            columna = int(input("Ingrese la posicion de la columna: "))
        dato = int(input("Ingrese el valor del dato: "))

        matriz[fila][columna] = dato
        seguir = input("Desea cambiar otro dato? s/n: ")

def validar_carga_aleatoria(fila: int, columna:int, cantidad_filas:int, cantidad_columnas:int) -> bool:
    return fila >= 0 and fila < cantidad_filas and columna >= 0 and columna < cantidad_columnas

def encontrar_valor(matriz:list, valor) -> int:
    for i in range(len(matriz)):
        for j in range(len(matriz[i])):
            if matriz[i][j] == valor:
                print(f"Se encontro: {valor} en la fila ({i} | columna {j})")
                return
    print(f"{valor} no se encontró :(")

def imprimir_diagonal_primaria(matriz:list) -> list:
    diagonal_primaria = [0] * len(matriz)
    for i in range(len(matriz)):
            diagonal_primaria[i] = matriz[i][i]
    return diagonal_primaria

def imprimir_diagonal_secundaria(matriz:list) -> list:
    diagonal_secundaria = [0] * len(matriz)
    for i in range(len(matriz)):
        diagonal_secundaria[i] = matriz[i][len(matriz) - 1 - i]
    return diagonal_secundaria

def sumar_diagonal_primaria(matriz:list) -> int:
    diagonal_primaria_total = 0
    for i in range(len(matriz)):
        diagonal_primaria_total += matriz[i][i]
    return diagonal_primaria_total

def sumar_diagonal_secundaria(matriz:list) -> int:
    diagonal_secundaria_total = 0
    for i in range(len(matriz)):
        diagonal_secundaria_total += matriz[i][len(matriz) - 1 - i]
    return diagonal_secundaria_total

matriz = incializar_matriz(3,3,0)
carga_secuencial(matriz)
mostrar_matriz(matriz)
carga_aleatoria(matriz,3,3)
mostrar_matriz(matriz)
encontrar_valor(matriz,55)
diagonal_primaria = imprimir_diagonal_primaria(matriz)
diagonal_secundaria = imprimir_diagonal_secundaria(matriz)
print(diagonal_primaria)
print(diagonal_secundaria)
totalprimaria = sumar_diagonal_primaria(matriz)
totalsecundaria = sumar_diagonal_secundaria(matriz)
print(totalprimaria)
print(totalsecundaria)