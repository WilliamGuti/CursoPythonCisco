# from random import randrange

# for i in range(10):
#     print(randrange(8))
posicion = ""
tablero = ["""
    ___________________
    |     |     |     |
    |  7  |  8  |  9  |
    |     |     |     |
    |-----------------|
    |     |     |     |
    |  4  |  X  |  6  |
    |     |     |     |
    |-----------------|
    |     |     |     |
    |  1  |  2  |  3  |
    |     |     |     |
    |-----------------|
    """
]

def DisplayBoard(board):
#
# la función acepta un parámetro el cual contiene el estado actual del tablero
# y lo muestra en la consola
#
    for i in tablero:
        print(i)
    return i

def EnterMove(board):
    while True:
        posicion = str(input("Ingresa un numero del 1 al 9 a jugar: "))
        if posicion == "0" or posicion == "10":
            break
        elif posicion == "1":
            for i in range(tablero):
                i = "O"

        print(tablero)
    print("Ingresa un numero correcto!")

EnterMove(posicion)
#
# la función acepta el estado actual del tablero y pregunta al usuario acerca de su movimiento, 
# verifica la entrada y actualiza el tablero acorde a la decisión del usuario
#

# def MakeListOfFreeFields(board):
# #
# # la función examina el tablero y construye una lista de todos los cuadros vacíos 
# # la lista esta compuesta por tuplas, cada tupla es un par de números que indican la fila y columna
# #

# def VictoryFor(board, sign):
# #
# # la función analiza el estatus del tablero para verificar si
# # el jugador que utiliza las 'O's o las 'X's ha ganado el juego
# #

# def DrawMove(board):
#
# la función dibuja el movimiento de la maquina y actualiza el tablero
#
