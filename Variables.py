# se crea una variable donde le puedes asignar cualquier cosa
var = 1
print(var)
#Se tiene permitido utilizar cuantas declaraciones de variables sean
#  necesarias para lograr el objetivo del programa, por ejemplo:
var = 1
balance_cuenta = 1000.0
nombreCliente = 'John Doe'
print(var, balance_cuenta, nombreCliente)
print(var)
# Se puede utilizar print() para combinar texto con variables utilizando
# el operador + para mostrar cadenas con variables, por ejemplo:
var = "3.7.1"
print("Versión de Python: " + var)

# se puede asignar nuevos valores a las variables por ejemplo:
var = 1
print(var)
var = var + 1
print(var)

# Taller
#Crear las variables: juan, maria, y adan.
# Asignar valores a las variables. El valor debe de ser igual al numero de manzanas que cada quien tenía.
# Una vez almacenados los números en las variables, imprimir las variables en una línea, y separar cada una de ellas con una coma.
# Después se debe crear una nueva variable llamada totalManzanas y se debe igualar a la suma de las tres variables anteriores.
# Imprime el valor almacenado en totalManzanas en la consola.
# SOLUCION
juan = 3 #variables 1
maria = 5 #variables 2
adan = 6 #variables 3
print ("Juan =",juan,"Maria =",maria,"adan =",adan) #impresion de cada variables
totalManzanas = juan+maria+adan #suma de todas las variables
print("el total de manzanas es= " , totalManzanas)  # impresion del total de manzanas