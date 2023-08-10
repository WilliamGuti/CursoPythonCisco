#Imagina una lista: no muy larga ni muy complicada, solo una lista simple que contiene algunos números enteros.
#  Algunos de estos números pueden estar repetidos, y esta es la clave. No queremos ninguna repetición. Queremos que sean eliminados.
#Tu tarea es escribir un programa que elimine todas las repeticiones de números de la lista. 
# El objetivo es tener una lista en la que todos los números aparezcan no más de una vez.

miLista = [1, 2, 4, 4, 1, 4, 2, 6, 2, 9] #definimos la lista
nuevaLista = [] #creamos una lista nueva donde almacenaremos el resultado final

for i in miLista: #hacemos un recorrido numero a numero
    if i not in nuevaLista: #verificamos que no este dentro de la nueva lista 
        nuevaLista += [i]   #y lo agregamos a la misma sin repetir el mismo caracter mas de una vez
print("La lista solo con elementos únicos:")
print(nuevaLista)   #imprimimos todo en la nueva lista