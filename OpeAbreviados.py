#declaracion de variables
y = 1
avion = 1
j = 1
var = 1
rem = 1
x = 1
i = 1
print(y)
print(avion)
# Pasar de esto:
y = y * 2
avion = avion + 1
print(y)
print(avion)

# A esto:
y *= 2
avion += 1
print(y)
print(avion)

i = i + 2 * j
i += 2 * j

var = var / 2
var /= 2

rem = rem % 10
rem %= 10

j = j - (i + var + rem) 
j -= (i + var + rem)

x = x ** 2 
x **= 2