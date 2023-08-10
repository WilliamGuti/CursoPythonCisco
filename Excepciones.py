# La palabra reservada try comienza con un bloque de código el cual puede o no estar funcionando correctamente.
#Después, Python intenta realizar la acción arriesgada: si falla, se genera una excepción y Python comienza a buscar una solución.
#La palabra reservada except comienza con un bloque de código que será ejecutado si algo dentro del bloque try sale mal 
# - si se genera una excepción dentro del bloque anterior try, fallará aquí, entonces el código ubicado después de la palabra
# clave except debería proporcionar una reacción adecuada a la excepción planteada.
#Se regresa al nivel de anidación anterior, es decir, se termina la sección try-except.

try:
    print("1")
    x = 1 / 0  # fallará aquí,
    print("2")
    print("Hola1")
except:
    print("Oh cielos, algo salio mal...")

print("3")

try:
    x = int(input("Ingresa un numero: "))
    y = 1 / x
except:
    print("Oh cielos, algo salio mal...")

print("FIN.")

## manera para manejar varias excepciones, pero el codigo en el editor podria incrementar considerablemente
## cuando una excepcion no esta dentro de las que hemos denominado, el codigo salta a la excepcion general
## cuando no hay una en general, python lanza su excepcion por defecto nombrando la linea y el tipo de excepcion
try:
    x = int(input("Ingresa un numero: "))
    y = 1 / x
    print(y)
except ZeroDivisionError:
    print("No puedes dividir entre cero, lo siento.")
except ValueError:
    print("Debes ingresar un valor entero.")
except:
    print("Oh cielos, algo salio mal...")

### Cada excepción cae en la primer coincidencia.
### La coincidencia correspondiente no tiene que especificar exactamente la misma excepción, es suficiente 
### que la excepción sea mas general (mas abstracta) que la lanzada.

try:
    y = 1 / 0
except ZeroDivisionError:
    print("Uuuppsss...")

print("FIN.")

try:
    y = 1 / 0
except ArithmeticError:
    print("Uuuppsss...")

print("FIN.")

print("THE END.")

#### la gerarquia de las excepciones se pueden tener en cuenta
        ## en este ejemplo podemo observar que se va a imprimir ARITMETICERROR
try:
    y = 1 / 0
except ArithmeticError:
    print("¡Problema aritmético!")
except ZeroDivisionError:
    print("¡División entre Cero!")

print("FIN.")

        ## pero en este caso, va ser ZERODIVISIONERROR
try:
    y = 1 / 0
except ZeroDivisionError:
    print("¡División entre Cero!")
except ArithmeticError:
    print("¡Problema aritmético!")

print("FIN.")    


##### Podemos hacer que las excepciones trabajen dentro de funciones y fuera de ellas
# dentro de la funcion
def badFun(n):
    try:
        return 1 / n
    except ArithmeticError:
        print("¡Problema aritmético!")
    return None
    badFun(0)  ## corregir este ejemplo si se llega a usar
print("FIN.")

# fuera de la funcion
def badFun(n):
    return 1 / n

try:
    badFun(0)
except ArithmeticError:
    print("¿Que pasó? ¡Se lanzo una excepción!")

print("FIN.")

###### se pueden manejar varias excepciones en una misma linea, separada por comas y entre parentesis

try:
    x = int(input("Ingresa un numero: "))
    y = 1 / x
    print(y)
except (ZeroDivisionError, ValueError):
    print("lo siento. Has causado una excepcion")
print('End')

####### instruccion RAISE permite crear nuestras propias excepciones
def badFun(n):
    try:
        return n / 0
    except:
        print("¡Lo hice otra vez!")
        raise

try:
    badFun(0)
except ArithmeticError:
    print("¡Ya veo!")

print("FIN.")
##
def badFun(n):
    raise ZeroDivisionError

try:
    badFun(0)
except ArithmeticError:
    print("¿Que pasó? ¿Un error?")

print("FIN.")
###
import math
from unittest import expectedFailure
def calcularRaiz(num1):
    
    if num1 <= 0:
        raise ValueError ('No se puede sacar raiz a un numero negativo')
    else:
        return math.sqrt(num1)

n1 = float(input('Introduce un numero: '))

try: 
    print(calcularRaiz(n1))
except ValueError as ErrorDeNumeroNegativo:
    print(ErrorDeNumeroNegativo)
print('Continuacion del codigo...')

######## la funcion FINALLY nos puede ayudar a ejecutar la linea de codigo despues de las excepciones
def division():
    try: 
        n1 = float(input('introduce el primer numero: '))
        n2 = float(input('introduce el segundo numero: '))
        print('La divicion entre: ' + str(n1) + ' y ' + str(n2) + ' es: ' + str(n1/n2))
    except ZeroDivisionError:
        print('No se puede dividir entre cero')
    except ValueError:
        print('introduce numeros')
    finally:
        print('Calculo realizado')
division()

######### funcion ASSERT nos sirve para validar los datos si han sido ingresados correctamente
######### Una excepción concreta generada por la instrucción de aserción cuando su argumento se 
######### evalúa como False (falso), None (ninguno), 0, o una cadena vacía.
######### de no ser asi, salta una excepcion, por ejemplo
import math
x = float(input("Ingresa un numero: "))
assert x >= 0.0

x = math.sqrt(x)

print(x)

########## Excepcion INDEXERROR
########## Una excepción concreta que surge cuando se intenta acceder al elemento de una secuencia
########## inexistente (por ejemplo, el elemento de una lista).

# el codigo muestra una forma extravagante
# de dejar el bucle

lista = [1, 2, 3, 4, 5]
ix = 0
doit = True

while doit:
    try:
        print(lista[ix])
        ix += 1
    except IndexError:
        doit = False

print('Listo')

#########################  EJEMPLOS #############################
def suma(num1, num2):
	return num1+num2

def resta(num1, num2):
	return num1-num2

def multiplica(num1, num2):
	return num1*num2

def divide(num1,num2):	
    try:
        return num1/num2
    except ZeroDivisionError:
        print('No se puede dividir entre cero')
        return 'Operacion invalida'	
while True:
    try:
        op1=(int(input("Introduce el primer numero: ")))
        op2=(int(input("Introduce el segundo numero: ")))		
        break

    except ValueError:
        print('Los valores introducidos son incorrectos, deben ser numero enteros')

operacion=input("Introduce la operacion a realizar (suma,resta,multiplica,divide): ")

if operacion=="suma":
	print(suma(op1,op2))

elif operacion=="resta":
	print(resta(op1,op2))

elif operacion=="multiplica":
	print(multiplica(op1,op2))

elif operacion=="divide":
	print(divide(op1,op2))

else:
	print ("Operacion no contemplada")


print("Operacion ejecutada. Continuacion de ejecucion del programa ")

# Tu tarea es escribir una función capaz de ingresar valores enteros y verificar si están dentro 
# de un rango especificado.
# Aceptar tres argumentos: una entrada, un límite inferior aceptable y un límite superior aceptable.
# Si el usuario ingresa una cadena que no es un valor entero, la función debe emitir el mensaje Error: 
# entrada incorrecta, y solicitará al usuario que ingrese el valor nuevamente.
# Si el usuario ingresa un número que está fuera del rango especificado, la función debe emitir el
# mensaje Error: el valor no está dentro del rango permitido (min..max) y solicitará al usuario que 
# ingrese el valor nuevamente.
# Si el valor de entrada es válido, será regresado como resultado.


def readint(prompt, min, max):
    while True:
        try:
            prompt = int(input("Ingresa un numero de -10 a 10: "))
            if prompt  <= max:
                if prompt >= min:
                    return prompt
                else:
                    print('Error: el valor no está dentro del rango permitido (-10..10)') 
            else:
                print('Error: el valor no está dentro del rango permitido (-10..10)') 
        except ValueError:
            print('Error, entrada incorrecta')
v = readint("Ingresa un numero de -10 a 10: ", -10, 10)

print("El numero es:", v)