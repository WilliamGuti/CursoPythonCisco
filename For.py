# #empieza desde cero y termina en 9
# for i in range(10):
#     print("El valor de i es actualmente", i)
# #empieza a partir del primer argumento dado, en este caos es 2
# for i in range (2, 8):
#     print("El valor de i es actualmente", i)
# #el tercer parametro indica la cantidad en la que debe avanzar
# for i in range(2, 8, 2):
#     print("El valor de i es actualmente", i)

# # break - ejemplo

# print("La instrucción de ruptura:")
# for i in range(1,6):
#     if i == 3:
#         break
#     print("Dentro del ciclo.", i)
# print("Fuera del ciclo.")

# # continue - ejemplo

# print("\nLa instrucción continue:")
# for i in range(1,6):
#     if i == 3:
#         continue
#     print("Dentro del ciclo.", i)
# print("Fuera del ciclo.")

# #ejemplo del break con contador
# numeroMayor = -99999999
# contador = 0

# while True:
#     numero = int (input ("Ingresa un número o escribe -1 para finalizar el programa:"))
#     if numero == -1:
#         break
#     contador = 1
#     if numero > numeroMayor:
#         numeroMayor = numero

# if contador != 0:
#     print("El número más grande es", numeroMayor)
# else:
#     print("No ha ingresado ningún número")

# #ejemplo del continue con contador
# numeroMayor = -99999999
# contador = 0

# numero = int (input("Ingresa un número o escribe -1 para finalizar el programa:"))

# while numero != -1:
#     if numero == -1:
#         continue
#     contador = 1

#     if numero > numeroMayor:
#         numeroMayor = numero
#     numero = int (input ("Ingresa un número o escribe -1 para finalizar el programa:"))

# if contador:
#     print("El número más grande es", numeroMayor)
# else:
#     print("No ha ingresado ningún número")
###################################################################
# for i in range(5):
#     print(f"Valor de la variable {i}")
###################################################################
# valido = False
# email = input("Ingresa tu correo: ")
# for i in range(len(email)):
#     if email[i] == "@":
#         valido = True
# if valido:
#     print("Email correcto")
# else:
#     print("Email incorrecto")

###################################################################
# Crea un programa que muestre los números impares del 1 al 100. Los números deberán 
# aparecer una al lado del otro sin salto de línea

# declarar una funcion:
# def cont():
#     for i in range(100):
#         if i % 2 != 0:
#             print(i , end=" ")
# cont()

###################################################################
# Crea un programa que pida por teclado introducir una contraseña. La contraseña no 
# podrá tener menos de 8 caracteres ni espacios en blanco. Si la contraseña es correcta, 
# el programa imprime “Contraseña OK”. En caso contrario imprime “Contraseña 
# errónea

# definimos las variables
# key = input('ingresa una contraseña mayor a 8 caracteres sin espacios: ')
# # definimos las funciones:
# def comprovacion(password):
#     keys = ''
#     cont = 0
#     for i in range(len(password)):
#         if password[i] == " ":
#             cont = 1  

#     if len(password) < 8 or cont > 1 :
#         return print('Contraseña erronea')
#     else:
#         return print("Contraseña ok")
# # Imprimimos el resultado
# comprovacion(key)

###################################################
# crea un programa que evalúe si una dirección de correo electrónico es válida o no en 
# función de si tiene “@” o “.” Hay que tener en cuenta que la dirección se considera 
# correcta si solo tiene una “@” y si tiene uno o más “.”

# Definimos las variables

# email = input('Ingresa tu correo electronico: ')
# Definir una funcion:
# def comprovar(email):
#     contadorPunto = 0
#     contadorArroba = 0
#     for i in range(len(email)):
#         if email[i] == '@':
#             contadorArroba = contadorArroba + 1

#         if email[i] == '.':
#             contadorPunto = 1 
        
#     if contadorPunto == 0 or contadorArroba != 1:
#         print('Correo Incorrecto')
#     else:
#         print('Correo correcto')
# # imprimimos el resultado
# comprovar(email)
