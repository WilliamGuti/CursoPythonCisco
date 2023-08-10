# hay ciertas situaciones donde una variable creada fuera de una funcion es visible dentro
# de una funcion, por ejemplo
# def miFuncion():
#     print("Conozco la variable?"  ,  var)
# var = 1
# miFuncion()
# print(var)

## si yo le agrego una variable con el mismo nombre de la variable que se encuentra fuera de la
## funcion, toma el valor que esta dentro de la funcion.
# # def miFuncion():
# #     var = 2
# #     print("Conozco la variable?"  ,  var)
# # var = 1
# # miFuncion()
# # print(var)

### la palabra reservada GLOBAL, permite modificar los valores de las variables que estan fuera de 
### las funciones
# # # def miFuncion():
# # #     global var
# # #     var = 2
# # #     print("¿Conozco a aquella variable?", var)

# # # var = 1
# # # miFuncion()
# # # print(var)

## ejemplo de indice de masa corporal
# def imc(peso, altura):
#     return peso / altura ** 2

# print(imc(52.5, 1.65))

# ### cuando querramos otros valoes en el sistema ingles
# def piespulgam(pies, pulgadas = 0.0):
#     return pies * 0.3048 + pulgadas * 0.0254


# def lbsakg(lb):
#     return lb * 0.45359237


# def imc(peso, altura):
#     if altura < 1.0 or altura > 2.5 or \
#     peso < 20 or peso > 200:
#         return None
    
#     return peso / altura ** 2


# print(imc(peso = lbsakg(176), altura = piespulgam(5, 7)))

# ## ejemplo para hallar si es o no un triangulo
# def esUnTriangulo(a, b, c):
#     if a + b <= c:
#         return False
#     if b + c <= a:
#         return False
#     if c + a <= b:
#         return False
#     return True

# print(esUnTriangulo (1, 1, 1))
# print(esUnTriangulo (1, 1, 3))

# # version compacta 
# def esUnTriangulo(a, b, c):
#     if a + b <= c or b + c <= a or \
#     c + a <= b:
#         return False
#     return True

# print(esUnTriangulo(1, 1, 1))
# print(esUnTriangulo(1, 1, 3))

##### Triangulo rectangulo
# def esUnTriangulo(a, b, c):
#     return a + b > c and b + c > a and c + a > b

# def esUnTrianguloRectangulo(a, b, c):
#     if not esUnTriangulo  (a, b, c):
#         return False
#     if c > a and c > b:
#         return c ** 2 == a ** 2 + b ** 2
#     if a > b and a > c:
#         return a ** 2 == b ** 2 + c ** 2
        
# a = float(input("Ingresa la longitud del primer lado: "))
# b = float(input("Ingresa la longitud del segundo lado: "))
# c = float(input("Ingresa la longitud del tercer lado: "))

# print(esUnTrianguloRectangulo(a, b, c))



################## EJEMPLO FACTORIAL
# def factorialFun(n):
#     if n < 0:
#         return None
#     if n < 2:
#         return 1
    
#     producto = 1
#     for i in range(2, n + 1):
#         producto *= i
#     return producto

# n = int(input("Ingresa un numero entero mayor a 1: "))
# for n in range (1,n+1):
#     print(n, factorialFun(n))

## otro camino POR RECURSIVIDAD PARA FACTORIAL
# def fac(n):
#     if n < 0:
#         return None
#     if n < 2:
#         return 1
#     return n * fac(n-1)
# n = int(input("Ingresa un numero entero mayor a 1: "))
# for n in range (1,n+1):
#     print(n, fac(n))

############# SERIE DE FIBONACCI
# def fib(n):
#     if n < 1:
#          return None
#     if n < 3:
#         return 1

#     elem1 = elem2 = 1
#     sum = 0
#     for i in range(3, n + 1):
#         sum = elem1 + elem2
#         elem1, elem2 = elem2, sum
#     return sum
# for n in range(1, 10): # probando
#     print(n, "->", fib(n))

## otro camino POR RECURSIVIDAD PARA FIBONACCI
# def fib(n):
#     if n < 1:
#         return None
#     if n < 3:
#         return 1
#     return fib(n - 1) + fib(n - 2)
# for n in range(1, 10): # probando
#     print(n, "->", fib(n))
