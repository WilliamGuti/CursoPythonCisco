# se empieza usando la palabra reservada def de DEFINE y seguido se le pone el nombre a la funcion
def mensaje():
    print("Ingresa un valor: ")

print("Se comienza aquí.")
mensaje()
print("Se termina aquí.")

# 
def mensaje():
    print("Ingresa un valor: ")

mensaje()
a = int(input())
mensaje()
b = int(input())
mensaje()
c = int(input())

#
def hola(nombre):    # definiendo una función
    print("Hola,", nombre)    # cuerpo de la función

nombre = input("Ingresa tu nombre: ")
hola(nombre)

#
def mensaje(numero):
    print("Ingresa un número:", numero)

mensaje(1)

## con dos parametros
def mensaje(que, numero):
    print("Ingresa", que, "número", numero)

# invocar la función
mensaje("teléfono", 11)
mensaje("precio", 5)
mensaje("número", "número")

def presentar(primerNombre, segundoNombre):
    print("Hola, mi nombre es", primerNombre, segundoNombre)

presentar("Luke", "Skywalker")
presentar("Jesse", "Quick")
presentar("Clark", "Kent")

## dandole argumentos a los parametros con el signo =
def presentar (primerNombre, segundoNombre):
    print("Hola, mi nombre es", primerNombre, segundoNombre)

presentar(primerNombre = "James", segundoNombre = "Bond")
presentar(segundoNombre = "Skywalker", primerNombre = "Luke")

## uso de palabras claves y de posicionamiento
def suma(a, b, c):
    print(a, "+", b, "+", c, "=", a + b + c)

# manda llamar la función suma aquí
suma(1,2,3)
suma(c = 1, a = 2, b = 3)
suma(3, c = 1, b = 2)

### uso de parametros pre definidos
def presentar(primerNombre='ana', segundoNombre="Smith"):
    print("Hola, mi nombre es", primerNombre, segundoNombre)

# mandar llamar la función aquí (invocarla)
presentar()
presentar('William')
presentar("Jorge", "Pérez")
presentar("Enrique")
presentar (primerNombre="Guillermo")

#### con 3 o mas parametros
def direccion(calle, ciudad, codigoPostal):
    print("Tu dirección es:", calle, ciudad, codigoPostal)

c = input("Calle: ")
cp = input("Código Postal: ")
cd = input("Ciudad: ")

direccion(c, cd, cp)

####### mas ejemplos ##########
# Ejemplo 1
def resta(a, b):
    print(a - b)

resta(5, 2)    # salida: 3
resta(2, 5)    # salida: -3


# Ejemplo 2
def resta(a, b):
    print(a - b)

resta(a=5, b=2)    # salida: 3
resta(b=2, a=5)    # salida: 3

# Ejemplo. 3
def resta(a, b):
    print(a - b)

resta(5, b=2)    # salida: 3
resta(5, 2)    # salida: 3


######## EL RETURN ########
### sin expresion
def felizAñoNuevo(deseos = True):
    print("Tres ...")
    print("Dos ...")
    print("Uno ...")
    if not deseos:
        return
    
    print("¡Feliz año nuevo!") 
felizAñoNuevo(False)

### con expresion
def funcion_aburrida():
    return 123

x = funcion_aburrida()

print ("La funcion_aburrida ha devuelto su resultado. Es: ", x)

### con expresion pero perdiendo el resultado
def funcion_aburrida():
    print("'Modo aburrimiento' ON.")
    return 123

print ("¡Esta lección es interesante!"  )
funcion_aburrida()
print("Esta lección es aburrida ...") 

###### EL NONE#########
valor = None
if valor == None:
    print("Lo siento, no tienes ningún valor") 

### 
def strangeFunction(n):
    if(n % 2 == 0):
        return True
print(strangeFunction(2))
print(strangeFunction(1)) 


#### con listas
def sumaDeLista(lst):
    sum = 0
    
    for elem in lst:
        sum += elem
    
    return sum
print(sumaDeLista([5, 4, 3])) 

### 
def strangeListFunction(n):
    strangeList = []
    
    for i in range(0, n):
        strangeList.insert(0, i)
    
    return strangeList

print(strangeListFunction(5))

# ejemplos
def suma(num1, num2):
    resultado = num1 + num2
    return resultado

almacenaResultado = suma(int(input("Ingresa una numero: ")),int(input("Ingresa un numero: ")))
print (almacenaResultado)

####################################

print("PROGRAMA PARA EVALUAR EDADES")
# declaracion de variables globales
edadUsuario = input("Ingresa tu edad: ")

#declaracion de funciones
def evaluar(edad):
        resultado = ''
        if edad >= 18:
                resultado = "Puede Pasar"
        else:
                resultado = "No puede pasar"
        return resultado
print(evaluar(int(edadUsuario)))