ListaSombrero = [1, 2, 3, 4, 5] #lista oculta en el sombrero
print("lista inicial", ListaSombrero)

# paso 1
num1 = int(input('Reemplace al numero central de la lista con un numero entero.')) 
ListaSombrero[2] = num1 
print("\n lista actualizada: ",ListaSombrero)

# paso 2 ELIMINAR UN ELEMENTO
del ListaSombrero[4]
print("\n lista acualizada: ", ListaSombrero)

#paso 3 LONGITUD DE LA LISTA ACTIALIZADA
print("\n LA LOGITUD DE LA LISTA ACTUAL ES: ", len(ListaSombrero))