# las listas son elementos que almacenan valores
# estos elementos se pueden modificar y se pueden imprimir
# ejemplo
numeros = [0,1,2,3,4,5,6,7,9,8]
print("la lista inicial es: ", numeros) # imprime la lista NUMEROS

# para poder modificar algun contenido de la lista se debe hacer

numeros[5] = 100
print(" \nla lista ha sido actualizada: ", numeros)

# pero adicional podemos cambiar un elemento de la lista
# por uno igual al que esta dentro de la esa lista

numeros[0] = numeros[5]
print( "\n la lista ha sido actualizada: ", numeros)

# adicional a eso podemos conocer la longitud de la lista con la funcio n LEN

print('\n la longitud de la lista es: ', len(numeros))

# los elementos dentros de las listas tambien se pueden eliminar, con la instruccion DEL o remove
# tambien la funcion POP sirve para eliminar el ultimo elemento de la lista
numeros.pop()
numeros.remove(5)
del numeros[7]
print("\nla longitud de la lista se ha modificado: ", len(numeros))
print("\nla lista, se ha actualizado: ", numeros)

# se pueden acceder a los elementos con numeros negativos, siempre y cuando estos
# se mantengan dentro de la lista

print( numeros[-4] )

numeros = [111, 7, 2, 1]
print(len(numeros))
print(numeros)

### metodo append, para incertar datos en la ultima posicion de las listas

numeros.append(4)

print(len(numeros))
print(numeros)

### metodo insert, para incertar datos en cualquier parte de la lista

numeros.insert(0,222)
print(len(numeros))
print(numeros)

### metodo para insertar varios elementos a la lista es con .extend
numeros.extend([11,12,13,14,15,16])
print(numeros)

### metodo para encontrar la posicion de un elemento, con .index
print(numeros.index(5))

# ejemplo
numeros.insert(1,333)
print(len(numeros))
print(numeros)

miLista = [] # creando una lista vacía

for i in range (5):
    miLista.append (i + 1)

print(miLista)

miLista = [] # creando una lista vacía

for i in range(5):
    miLista.insert(0, i + 1)

print(miLista)

# suma de los elementos dentro de la listas 
miLista = [10, 1, 8, 3, 5]
suma = 0

for i in miLista:
    suma += i

print(suma)

## sumando o concatenando listas
miLista1 = [1,2,3,4,5,6] 
miLista2 = [7,8,"ana","Wilsom",9]
miLista3 = miLista1 + miLista2
print(miLista3)


## multiplicar listas solo con el simbolo de multiplicacion *
miLista4 = [1,1,1,1,1,1] * 3

#cambiar el orden de las listas 
miLista = [10, 1, 8, 3, 5]

miLista [0], miLista [4] = miLista [4], miLista [0]
miLista [1], miLista [3] = miLista [3], miLista [1]

print(miLista)
miLista = [10, 1, 8, 3, 5]
longitud = len(miLista)

for i in range (longitud // 2):
    miLista[i], miLista[longitud-i-1] = miLista[longitud-i-1], miLista[i]

print(miLista)  

# in y Not in
miLista = [0, 3, 12, 8, 2]

print(5 in miLista)
print(5 not in miLista)
print(12 in miLista)

#numero mas grande 
miLista = [17, 3, 11, 5, 1, 9, 7, 15, 13]
mayor = miLista [0]

for i in miLista:
    if i > mayor:
        mayor = i

print(mayor)

#encontrar un numero
miLista = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
Encontrar = 5
Encontrado = False

for i in range(len(miLista)):
    Encontrado = miLista[i] == Encontrar
    if Encontrado:
        break

if Encontrado:
    print("Elemento encontrado en el índice", i)
else:
    print("ausente")

# numeros ganadores de loteria 
sorteados = [5, 11, 9, 42, 3, 49]
seleccionados = [3, 7, 11, 42, 34, 49]
aciertos = 0

for numeros in seleccionados:
    if numeros in sorteados:
        aciertos += 1

print(aciertos)

#### para transformar una lista en tupla es con el nombre reservado TUPLE
miLista = ["William", 28 , 2 , 1996]
miTupla = tuple(miLista)
print(miTupla)