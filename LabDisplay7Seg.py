# Tu tarea es escribir un programa que puede simular el funcionamiento de un display de siete segmentos, aunque vas a usar 
# LEDs individuales en lugar de segmentos.
# Cada dígito es construido con 13 LEDs (algunos iluminados, otros apagados, por supuesto), así es como lo imaginamos:

  # ### ### # # ### ### ### ### ### ### 
  #   #   # # # #   #     # # # # # # # 
  # ### ### ### ### ###   # ### ### # # 
  # #     #   #   # # #   # # #   # # # 
  # ### ###   # ### ###   # ### ### ###

#Tu código debe mostrar cualquier número entero no negativo ingresado por el usuario.
# Consejo: puede ser muy útil usar una lista que contenga patrones de los diez dígitos.
numeros =[
[
'###',
'# #',
'# #',
'# #',
'###',
],
[
'  #',
'  #',
'  #',
'  #',
'  #',
],
[
'###',
'  #',
'###',
'#  ',
'###',
],
[
'###',
'  #',
'###',
'  #',
'###',
],
[
'# #',
'# #',
'###',
'  #',
'  #',
],
[
'###',
'#  ',
'###',
'  #',
'###',
],
[
'###',
'#  ',
'###',
'# #',
'###',
],
[
'###',
'  #',
'  #',
'  #',
'  #',
],
[
'###',
'# #',
'###',
'# #',
'###',
],
[
'###',
'# #',
'###',
'  #',
'###',
]
]
numero = input("Dame un numero: ")
for i in range(5):
    renglon = ""                       # Empezar con renglón vacío
    for cifra in numero:               # Crear el renglón
        cifra= int(cifra)              # Recorriendo cada cifra
        renglon += numeros[cifra][i]   # y añadiéndola al renglón
        renglon += " "                 # mas un espacio en blanco
    print(renglon)                     # Imprimir el renglón creado