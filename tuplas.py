# Una tupla es una lista de elementos bien sean int, float, chart etc...
# que no se pueden modificar
# ejemplo
# tupla1 = (1,2,3,4) # tupla con elementos
# tupla2 = () # tupla vacia
# tupla3 = (1,) # tupla con un solo elemento
# tupla11= 1,2,3 # otra forma de crearla sin parentesis
# print (tupla1)
# ## otro ejemplo para aecceder a los elementos
# miTupla = (1, 10, 100, 1000)

# print(miTupla[0])
# print(miTupla[-1])
# print(miTupla[1:])
# print(miTupla[:-2])

# for elem in miTupla:
#     print(elem)

### ejemplo de como sumar, multiplicar y ver cuantos caracteres hay en una tupla
# miTupla = (1, 10, 100)

# t1 = miTupla + (1000, 10000)
# t2 = miTupla * 3

# print(len(t2)) ## SIRVE PARA AVERIGUAR LA LONGITUD DE LA TUPLA
# print(t1)
# print(t2)
# print(10 in miTupla)
# print(-10 not in miTupla)

#### se pueden intercambiar los valores de las tuplas
# var = 123

# t1 = (1, )
# t2 = (2, )
# t3 = (3, var)

# t1, t2, t3 = t2, t3, t1

# print(t1, t2, t3)

######### convertir una tupla en una lista con la palabra reservada LIST
# mitupla = ("William", 28, 2 ,1996)
# miLista = list(mitupla)
# print(miLista)

#### para poder averiguar cuantos elementos se repiten dentro de la tupla se usa 
#### la palabra reservada COUNT 
# miLista = ["William", 28 , 2 , 1996 , 2]
# miTupla = tuple(miLista)
# print(miTupla.count(2))

##### Completa el código para emplear correctamente el método count() para encontrar
##### la cantidad de 2 duplicados en la tupla siguiente.
# tup = 1, 2, 3, 2, 4, 5, 6, 2, 7, 2, 8, 9
# duplicado = tup.count(2)
# print(duplicado)

####### ASIGNAR VALORES DE LA TUPLA A VARIABLES
# miTupla = ("William", 28 , 2 , 1996)
# nombre, dia, mes, anio = miTupla
# print(nombre, dia, mes, anio , end="")

#Escribe un programa que convierta la lista l en una tupla.
# l = ["carro", "Ford", "flor", "Tulipán"]
# print(l)
# t = tuple(l)
# print(t)

#Escribe un programa que convierta la tupla colores en un diccionario.
# colores = (("verde", "#008000"), ("azul", "#0000FF"))
# colDict = dict(colores)
# print(colDict)

i = 10/0
print(i)