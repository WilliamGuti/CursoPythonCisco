# # Lee e imprime el numero mas grande
# #lee tres números
# numero1 = int (input("Ingresa el primer número:"))
# numero2 = int (input("Ingresa el segundo número:"))
# numero3 = int (input("Ingresa el tercer número:"))

# #asumimos temporalmente que el primer número
# #es el más grande
# #lo verificaremos pronto
# nmasGrande = numero1

# #comprobamos si el segundo número es más grande que el mayor número actual
# #y actualiza el número más grande si es necesario
# if numero2 > nmasGrande:
#     nmasGrande = numero2

# #comprobamos si el tercer número es más grande que el mayor número actual
# #y actualiza el número más grande si es necesario
# if numero3 > nmasGrande:
#     nmasGrande = numero3

# #imprimir el resultado
# print("El número más grande es:", nmasGrande)

# # ejemplo con una funcion MAX o MIN

# # lee tres números
# numero1 = int(input("Ingresa el primer número:"))
# numero2 = int(input("Ingresa el segundo número:"))
# numero3 = int(input("Ingresa el tercer número:"))

# # verifica cuál de los números es el mayor
# # y pásalo a la variable de mayor número

# numeroMayor = max(numero1,numero2,numero3)

# # imprimir el resultado
# print("El número más grande es:", numeroMayor)

# lee las cadenas
# x = input("ingrese la palabra Espatifilo")
# if x == 'Espatifilo':
#     print("Si, ¡El Espatifilo es la mejor planta de todos los tiempos!")
# elif x == 'espatifilo':
#     print("No, ¡quiero un gran Espatifilo!")
# else:
#     print("!Espatifilo! ¡No", x ,"!")
