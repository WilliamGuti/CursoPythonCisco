# declaracion de variables
bloques = int(input("Ingrese el número de bloques:"))
contador = 0
# uso de ciclo
while bloques > 0:
    contador += 1
    bloques = bloques - contador
if bloques < 0:
    contador -= 1
print("La altura de la pirámide:", contador)
print("La cantidad de bloques es:", bloques)