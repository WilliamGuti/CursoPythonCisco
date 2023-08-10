# # 6. Escribir un programa que pida al usuario que introduzca una frase en la consola y una vocal, y después 
# # muestre por pantalla la misma frase pero con la vocal introducida en mayúscula.
# def may(frase,vocal):
#     fraseMay = ''
#     for letra in frase:
#         if letra == vocal:
#             fraseMay += letra.upper()
#         else:
#             fraseMay += letra
#     return fraseMay

# frase = input('introduzca una frase: ')
# vocal = input('introduza una vocal: ')
# print(may(frase,vocal))


# # # 7. Escribir un programa que pregunte el correo electrónico del usuario en la consola y muestre por pantalla otro correo 
# # # electrónico con el mismo nombre (la parte delante de la arroba @) pero con dominio ceu.es.
# # correo = input('ingrese su correo: ')
# # print(correo[:correo.find('@')] + '@ceu.es')
# def dom(correo):
#     email=''
#     dominio = '@'
#     for letra in correo:
#         if letra == dominio and '@':
#             email += '@ceu.es'
#         else:
#             email+=letra
#     return email
# correo = input('ingrese correo: ')
# print(dom(correo))

# # 8. Escribir un programa que pregunte por consola el precio de un producto en euros con dos decimales y muestre por 
# # pantalla el número de euros y el número de céntimos del precio introducido.

# def product(producto):
#     totalP = ''
#     for num in producto:
#         if num == :
#     return totalP

# producto = float(input('cual es el precio del producto en euros? '))
# print('son ', producto, 'y', centavos )



# list = [x*x for x in range(5)]
# def fun (lst):
#         del lst[lst[2]]
#         return lst
# print(fun(list))
# a= 1
# b =0
# a = a^b
# b = a^b
# a = a^b
# print(a,b)

#####################################################
# # Crea un programa que pida dos números por teclado. El programa tendrá una función 
# # llamada “DevuelveMax” encargada de devolver el número más alto de los dos
# # introducidos.

# # creamos los datos para ingresar
# num1 = int(input("Ingresa primer numero : "))
# num2 = int(input("Ingresa segundo numero : "))
# # declaramos la funcion
# def DevuelveMax(numero1,numero2):
#         mayor = numero1
#         if numero2 > numero1:
#                 mayor = numero2
#         elif numero2 == numero1:
#                 mayor = "Numeros iguales"
#         return mayor
# print(DevuelveMax(num1,num2))

#####################################################
# Crea un programa que pida por teclado “Nombre”, “Dirección” y “Tfno”. Esos tres datos 
# deberán ser almacenados en una lista y mostrar en consola el mensaje: “Los datos 
# personales son: nombre apellido teléfono” (Se mostrarán los datos introducidos por 
# teclado).
# definir entrada de datos
# nombre = input("ingresa tu nombre: ")
# direccion = input("Ingresa tu Direccion: ")
# telefono = int(input("Ingresa tu numero telefonico: "))
# # crear la lista
# lista = [nombre, direccion,telefono]
# #imprimir resultado
# print("Los datos personales son:" , lista[0],lista[1],lista[2])

##########################################
# Crea un programa que pida tres números por teclado. El programa imprime en consola 
# la media aritmética de los números introducidos.
# num1 = float(input("Ingresa un numero"))
# num2 = float(input("Ingresa un numero"))
# num3 = float(input("Ingresa un numero"))
# media = (num1+num2+num3) / 3
# print(media)


#########################################
# sistema de becas para alumnos con condicionales
# distancia = int(input("ingresa la distancia: "))
# numHermanos  = int(input("Ingresa el numero de hermanos: "))
# salario = int(input("ingresa el salario: "))

# def becas(a,b,c):
#         if a >= 40 and b >= 2 or c <= 20000:
#                 return "Tiene beca"
#         else:
#                 return "No tiene beca"

# print(becas(distancia,numHermanos,salario))

# email = False
# miEmail = input('introduce tu correo: ')
# for i in miEmail:
#     if i == '@' and i == '.com':
#         email = True

# if email == True:
#     print('Correo valido')
# else:
#     print('Correo no valido')

# este código causa la excepción MemoryError
# advertencia: ejecutar este código puede ser crucial
# para tu sistema operativo
# ¡no lo ejecutes en entornos de producción!

# Tu tarea es escribir una función capaz de ingresar valores enteros y verificar si están dentro 
# de un rango especificado.
# Aceptar tres argumentos: una entrada, un límite inferior aceptable y un límite superior aceptable.
# Si el usuario ingresa una cadena que no es un valor entero, la función debe emitir el mensaje Error: 
# entrada incorrecta, y solicitará al usuario que ingrese el valor nuevamente.
# Si el usuario ingresa un número que está fuera del rango especificado, la función debe emitir el
# mensaje Error: el valor no está dentro del rango permitido (min..max) y solicitará al usuario que 
# ingrese el valor nuevamente.
# Si el valor de entrada es válido, será regresado como resultado.


print(float('1,3'))