# se debe asignar a un avariables el valor de input
x = input()
# tambien se puede asignar texto dentro de el, no afecta nada en el codigo
y = input("Ingresa un dato para la variable Y: ")
# pero como queda guardado en tipo str, se puede cambiar a tipo int o float
z = int(input("Ingresa un datos para la variable Z: "))
J = float(input("Ingresa un datos para la variable J: "))

#ejemplos
print(x , y)
print(z * J)
print(x,J)

# ejemplo 2
cateto_a = float(input("Inserta la longitud del primer cateto: "))
cateto_b = float(input("Inserta la longitud del segundo cateto "))
hipo = (cateto_a**2 + cateto_b**2) ** .5
print("La longitud de la hipotenusa es: ", hipo)

#concatenacion (+)
nom = input("¿Me puedes dar tu nombre por favor? ")
ape = input("¿Me puedes dar tu apellido por favor? ")
print("Gracias.")
print("\nTu nombre es " + nom + " " + ape + ".")

# replicacion (*)
print("x"*3)

#ejemplo 3
a = float(input("ingresa un dato: ")) # ingresa un valor flotante para la variable a aquí
b = float(input("ingresa un dato: ")) # ingresa un valor flotante para la variable b aquí
sumVariables = (a +  b)
resVariables = (a - b)
mulVariables = (a * b)
divVariables = (a // b)
print("la suma es:" , sumVariables) # muestra el resultado de la suma aquí 
print("la resta es:" , resVariables) # muestra el resultado de la resta aquí
print("la multiplicacion es:" , mulVariables) # muestra el resultado de la multiplicación aquí
print("la division es:" , divVariables) # muestra el resultado de la división aquí

print("\n¡Eso es todo, amigos!")

# ejemplo 3
x = float(input("Ingresa el valor para x: "))
y = 1/(x+1/(x+1/((x)+1/x)))
print("y =", y)