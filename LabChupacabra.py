#Diseña un programa que use un ciclo while y le pida continuamente
#al usuario que ingrese una palabra a menos que ingrese "chupacabra"
#como la palabra de salida secreta, en cuyo caso el mensaje
#"¡Has dejado el ciclo con éxito". Debe imprimirse en la pantalla 
#y el ciclo debe terminar.

#No imprimas ninguna de las palabras ingresadas por el usuario.
#Utiliza el concepto de ejecución condicional y la declaración break.

#declaramos la variable
x = '0'
#declaramos el ciclo con la condicional
while x != "chupacabra":
    x = input("ingrese la palabra clave: ")
    if x == "chupacabra":
        print("has dejado el ciclo")
        break