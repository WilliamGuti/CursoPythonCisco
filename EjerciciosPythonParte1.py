###############################################################################
# 1.Definir una función max() que tome como argumento dos números y devuelva el mayor de ellos. 
# (Es cierto que python tiene una función max() incorporada, pero hacerla nosotros mismos es un muy buen ejercicio.


# def maximo(num1,num2):
#     numMAyor = 0
#     if num1 >= num2:
#         numMayor = num1
#     else:
#         numMayor = num2
#     return(numMayor)
# num1 = int(input('ingrese un numero: '))
# num2 = int(input('ingrese otro numero: '))
# print(maximo(num1,num2))

# # 2.Definir una función max_de_tres(), que tome tres números como argumentos y devuelva el mayor de ellos.
# def max_de_tres(num1,num2,num3):
#     numMayor = 0
#     if num1 >= num2 and num1 >= num3:
#         numMayor = num1
#     elif num2 >= num1 and num2 >= num3:
#         numMayor = num2
#     elif num3 >= num1 and num3 >= num2:
#         numMayor = num3
#     return(numMayor)

# num1 = int(input('ingrese el primer numero: '))
# num2 = int(input('ingrese el segundo numero: '))
# num3 = int(input('ingrese el tercer numero: '))
# print(max_de_tres(num1,num2,num3))

# # 3.Definir una función que calcule la longitud de una lista o una cadena dada. 
# # (Es cierto que python tiene la función len() incorporada, pero escribirla por nosotros mismos resulta un muy buen ejercicio).

# def longitud(cadena):
#     mayor = 0
#     for letra in cadena:
#         mayor += 1
#     return (mayor)
# cadena = input(' ingrese una letra ')
# print(longitud(cadena))

# # 4. Escribir una función que tome un carácter y devuelva True si es una vocal, de lo contrario devuelve False

# def vocal(x):
#     if x == 'a' or x == 'e' or x == 'i' or x == 'o' or x == 'u' :
#         return True
#     elif  x == 'A' or x == 'E' or x == 'O' or x == 'U' or x == 'I' :
#         return True
#     else :
#         return False

# x = input('ingrese una letra: ')
# print(vocal(x))

# 5. Escribir una función sum() y una función multip() que sumen y multipliquen respectivamente todos los números de una lista.
# Por ejemplo: sum([1,2,3,4]) debería devolver 10 y multip([1,2,3,4]) debería devolver 24.
# 
# def filas(fila,columna):
#     lista = []    
#     for i in range(fila):
#         lista.append([0]*columna) # definimos de como sera la lista o matriz

#     for f in range(fila):
#         for c in range(columna):
#             lista[f][c] = int(input('elemento %d,%d :''' % (f,c))) # agregamos elemenos dentro de la lista o matriz
   
#     return(lista)

# def sum(sumas):
#     lista = filas(fila,columna)
#     suma = 0
#     for s in lista:
#         suma += s
#     return(suma)

# def multipli(multiplicacion):
#     multi = 1
#     lista = filas(fila,columna)
#     for m in lista:
#         multi *= m    
#     return(multi)

# fila = int(input('ingrese la cantidad de filas: '))
# columna = int(input('ingrese la cantidad de columnas: '))

# print(filas(fila,columna))

# print(sum(sumas=int))

# print(multipli(multiplicacion=int))

# def sum(lista):
#     suma = 0
#     for s in lista:
#         suma += s
#     return(suma)
# lista = [1,2,3]
# print(sum(lista))

# def multipli(lista):
#     multi = 1
#     for m in lista:
#         multi *= m    
#     return(multi)

# 6. Definir una función inversa() que calcule la inversión de una cadena.
# Por ejemplo la cadena "estoy probando" debería devolver la cadena "odnaborp yotse"
# def inversa(cadena):
#     invertida = ""
#     cont = len(cadena)
#     indice = -1
#     while cont >= 1:
#         invertida += cadena[indice]
#         indice = indice + (-1)
#         cont -= 1
#     return invertida

# print = inversa("william")


# 7.Definir una función es_palindromo() que reconoce palíndromos 
# (es decir, palabras que tienen el mismo aspecto escritas invertidas), ejemplo: es_palindromo ("radar") tendría que devolver True.
# def esPalindromo(palabra):
#     palindromoIzq = 0
#     palindromoDer = len(palabra) - 1
#     while palindromoDer >= palindromoIzq:
#         if not palabra[palindromoIzq] == palabra[palindromoDer]:
#             return False
#         palindromoIzq += 1
#         palindromoDer -= 1
#     return True
# print(esPalindromo('ana'))
#8. Definir una función superposicion() que tome dos listas y
# devuelva True si tienen al menos 1 miembro en común o devuelva False de lo contrario. Escribir la función usando el bucle for anidado.
# def superposicion(lista1,lista2):
#     for List1 in lista1:
#         for List2 in lista2:
#             if List1 == List2:
#                 print(True)
#                 return(1)
#     print(False)            
#     return (0)
# superposicion([1,2,3,4],[4,5,6,7])

# 9. Definir una función generar_n_caracteres() que tome un entero n 
# y devuelva el caracter multiplicado por n. Por ejemplo: generar_n_caracteres(5, "x") debería devolver "xxxxx".
# def generarCaracter(letra,multiplicador):
#     print (multiplicador * letra)
# generarCaracter('w',5)

# 10 . Definir un histograma procedimiento() que tome una lista de números enteros
# e imprima un histograma en la pantalla. Ejemplo: procedimiento([4, 9, 7]) debería imprimir lo siguiente:
# ****
# *********
# *******
# def procedimiento(lista):
#     for i in lista:
#         print (i * "*")
# procedimiento([5,3,4])