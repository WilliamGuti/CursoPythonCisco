#declaracion de variables
c0 = int(input('ingresa un numero: '))
contador = 0
# ciclo
while c0 != 1 :
    if c0 % 2 == 0:
        c0 = c0 / 2
    else:
        c0 = (c0 * 3) + 1
    contador += 1
    print(int(c0)) # imprime los valores intermedios
print("el numero de pasos fue: ", contador) # imprime los pasos tomados