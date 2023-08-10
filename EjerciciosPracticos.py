#Crea un bucle for que cuente de 0 a 10, e imprima números impares en la pantalla. Usa el esqueleto de abajo:
print("*-*primer ejercicio!*-*")
x = 0
for x in range (0 , 11):
    if x % 2 == 0:
        continue
    print(x)
print('segunda solucion')
for i in range(0, 11):
    if i % 2 != 0:
        print(i)

#Crea un bucle while que cuente de 0 a 10, e imprima números impares en la pantalla. Usa el esqueleto de abajo:
print("\n*-*segundo ejercicio!*-*")
y = 0
while y < 10:
    y += 1
    if y % 2 == 0:
        continue
    print(y)
print('segunda solucion')
y = 1
while y < 11:
    if y % 2 != 0:
        print(y)
    y += 1

#Crea un programa con un bucle for y una declaración break. El programa debe iterar sobre los caracteres
#en una dirección de correo electrónico, salir del bucle cuando llegue al símbolo @ e imprimir la parte
#antes de @ en una línea. Usa el esqueleto de abajo:
print("\n*-*tercer ejercicio!*-*")
for ch in "john.smith@pythoninstitute.org":
    if ch == "@":
        break
    print(ch)
print('segunda solucion')
for ch in "john.smith@pythoninstitute.org":
    if ch == "@":
        break
    print(ch, end="")

#Crea un programa con un bucle for y una declaración continue. El programa debe iterar sobre una cadena de dígitos,
#reemplazar cada 0 con x, e imprimir la cadena modificada en la pantalla. Usa el esqueleto de abajo:
print("\n*-*cuarto ejercicio!*-*")
for digit in "0165031806510":
    if digit == "0":
        digit = 'X' # línea de código
         # línea de código
    print(digit, end="") # línea de código 

print("\nsegunda solucion")
for digit in "0165031806510":
    if digit == "0":
        print("x", end="")
        continue
    print(digit, end="")

    