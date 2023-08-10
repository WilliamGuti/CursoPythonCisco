# la palabra reservada IMPORT nos permite importar librerias de python
# con la siguiente sintaxis
# import math
# print(math.sin(math.pi/2))

# # las entidades no se afectan entre si
# import math

# def sin(x):
#     if 2 * x == pi:
#         return 0.99999999
#     else:
#         return None

# pi = 3.14

# print(sin(pi/2))
# print(math.sin(math.pi/2))

# from math import sin, pi

# print(sin(pi/2))

# pi = 3.14

# def sin(x):
#     if 2 * x == pi:
#         return 0.99999999
#     else:
#         return None

# print(sin(pi/2))

## para importar todas las entiedaddes de un modulo es:
# from module import *

# para darle un 'alias' a un modulo se puede hacer de la siguiente manera
# import module as alias
# ejemplos
# import math as m

# print(m.sin(m.pi/2))
# from math import pi as PI, sin as sine

# print(sine(PI/2))

# import math
# dir(math)
# from math import pi, radians, degrees, sin, cos, tan, asin

# ad = 90
# ar = radians(ad)
# ad = degrees(ar)

# print(ad == 90.)
# print(ar == pi / 2.)
# print(sin(ar) / cos(ar) == tan(ar))
# print(asin(sin(ar)) == ar)
# from math import e, exp, log

# print(pow(e, 1) == exp(log(e)))
# print(pow(2, 2) == exp(2 * log(2)))
# print(log(e, e) == exp(0))
#### algunos modulos de math
# from math import ceil, floor, trunc, factorial, hypot

# x = 1.4
# y = 2.6

# print(floor(x), floor(y))
# print(floor(-x), floor(-y))
# print(ceil(x), ceil(y))
# print(ceil(-x), ceil(-y))
# print(trunc(x), trunc(y))
# print(trunc(-x), trunc(-y))
# print(factorial(5))
# print(hypot(5,3))

#############################################################
# modulo random
# from random import random

# for i in range(5):
#     print(random())

# from random import random, seed

# seed(0)

# for i in range(5):
#     print(random())

# from random import randrange, randint

# print(randrange(1), end=' ') # escoge un numero aleatorio no mayor a 1
# print(randrange(0, 1), end=' ') # escoge un numero aleatorio iniciando en 0 y terminando en 1
# print(randrange(0, 1, 1), end=' ') # escoge un numero aleatorio iniciando en 0 y terminando en 1 en paso de 1 a 1
# print(randint(0, 1)) La función randint(a, b) genera un número entero entre 0 y 1, ambos incluidos. a debe ser inferior o igual a 1.

# from random import randint

# for i in range(10):
#     print(randint(1, 10), end=',')

# from random import choice, sample

# lst = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

# print(choice(lst)) # coge un numero random
# print(sample(lst, 5)) # coge un numero random en un rango
# print(sample(lst, 10))


##############################################
# modulo platform permite acceder a los datos de la 
# plataforma subyacente, es decir, hardware, sistema operativo e 
# información sobre la versión del intérprete.
# from platform import platform

# print(platform())
# print(platform(1))
# print(platform(0, 1))

# para conocer el nombre generico del procesador
# from platform import machine

# print(machine())

# devuelve el nombre real del procesador
# from platform import processor

# print(processor())

# devuelve el nombre del sistema operativo
# from platform import system

# print(system())

# version del sistema operativo
# from platform import version

# print(version())

# conocer la version de python
# from platform import python_implementation, python_version_tuple

# print(python_implementation())

# for atr in python_version_tuple():
#     print(atr)


#######################################
# impoetar un modulo desde una carpeta
#path se utiliza para examinar la ruta 
#y sys para verificar el valor

# from sys import path
# path.append('C:\\Users\\William\Desktop\\CursoPythonCisco\\MyModulo')
# import miModulo