# # Almacenaremos el número más grande actual aquí
# numeroMayor = -999999999

# # Ingresa el primer valor
# numero = int(input ("Introduzca un número o escriba -1 para detener:"))

# # Si el número no es igual a -1, continuaremos
# while numero != -1:
#    # ¿Es el número más grande que el número más grande?
#    if numero > numeroMayor:
#        # Sí si, actualiza el mayor númeroNúmero
#        numeroMayor = numero
#    # Ingresa el siguiente número
#    numero = int (input("Introduce un número o escribe -1 para detener:"))

# # Imprimir el número más grande
# print ("El número más grande es:", numeroMayor)

# programa que lee una secuencia de números
# y cuenta cuántos números son pares y cuántos son impares
# programa termina cuando se ingresa cero

# numerosImpares = 0
# numerosPares = 0

# # lee el primer número
# numero = int (input ("Introduce un número o escriba 0 para detener:"))

# # 0 termina la ejecución
# while numero != 0:
#     # verificar si el número es impar
#     if numero % 2 == 1:
#         # aumentar el contador de números impares
#         numerosImpares += 1
#     else:
#         # aumentar el contador de números pares
#         numerosPares += 1
#     # lee el siguiente número
#     numero = int (input ("Introduce un número o escriba 0 para detener:"))

# # imprimir resultados
# print("Números impares: ", numerosImpares)
# print("Números pares: ", numerosPares)

# i = 1
# while i <= 10:
#     print('ejecucion' , str(i))
#     i = i + 1
# print('Termino la ejecucion')

# edad = 0
# while edad <= 0:
#     edad = int(input('ingresa tu edad:'))
# print('Correcto')

######################## 
# ejercicio comprovacion de la raiz de un numero
# import math

# print('Programa para calcular la raiz cuadrada de un numero')
# numero = int(input('Introduce un numero: '))
# intentos = 0

# while numero < 0 :
#     print('no se puede hallar la raiz cuadrada de numeros negativos')
    
#     numero = int(input('Introduce un numero: '))
#     if numero < 0:
#         intentos += 1

#     if intentos == 2:
#         print('Te has consumido todos los intentos')    
#         break

# if intentos < 2:
#     solucion = math.sqrt(numero)
#     print('La raiz cuadrada de' , numero , 'es' , solucion)

#################################################################################
# Crea un programa que pida números infinitamente. Los números introducidos deben 
# ser cada vez mayores. El programa finalizará cuando se introduce un número menor que 
# el anterior.

# i = 0
# numero = int(input('Introduce un numero: '))
# while i < numero:
#     print('Intentalo de nuevo')
#     i = numero
#     numero = int(input('Introduce un numero: '))
    
# print('Lo haz logrado!')

#################################################################################

# Crea un programa que pida números positivos indefinidamente. El programa termina 
# cuando se introduce un número negativo. Finalmente el programa muestras la suma de 
# todos los números introducidos

# num = int(input('Introduce un numero positivo: '))
# suma = 0

# while num > 0:
#     suma = suma + num
#     num = int(input('Introduce un numero positivo: '))
# print(suma)

