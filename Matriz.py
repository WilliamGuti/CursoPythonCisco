# MATRIX ( ARRAY  , ARREGLO)
# ES UNA COLECCION O CONJUNTO DE ELEMENTOS FORMADOS
# POR FILAS Y COLUMNAS
# TAMBIEN SE PUEDEN HACER UNA LISTA DE LISTAS DONDE REPRESENTAN
# FILAS Y COLUMNAS TAMBIEN
  
# # EJEMPLO
# lista = [1,2,3,4] # esto es una lista
# matrix = [[4,3,8,],[1,6,5],[2,0,9]]  # esto una matriz
# matrix [0][0] = 7 # modificar un elemento de la matriz
# print(matrix [0] [0]) #para acceder a una posicion de la matrix
# print(len(matrix))    #para medir el tama;o de una matriz
# print(len(matrix[0]))    #para medir la cantidad de columnas de una matriz


# # CREACION DE MATRICES

# matriz = [] # crear una matriz

# filas = int(input('ingrese la cantidad de filas')) # ingrear la cantidad de filas
# columnas = int(input('ingrese la cantidad de columnas')) # ingresar la cantidad de columnas
# for i in range (filas):
#     matriz.append([0]*columnas)  # agregar elementos dentro de la matriz

# # poner valores que quiere el usuario 
# # usar dos bucles anidados
# for f in range(filas):
#     for c in range(columnas):
#         matriz[f][c]= int(input('elemento %d,%d :''' % (f,c)))

# # matriz[0][0] = 1 # modificar un elemento de la matriz
# print(matriz)

# APLICACIONES


# EMPTY = "-"
# TORRE = "TORRE"
# tablero = []

# for i in range(8):
#     fila = [EMPTY for i in range(8)]
#     tablero.append (fila)

# tablero[0][0] = TORRE
# tablero[0][7] = TORRE
# tablero[7][0] = TORRE
# tablero[7][7] = TORRE

# print(tablero),