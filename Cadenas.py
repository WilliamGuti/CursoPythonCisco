#Literales son notaciones para representar valores 
# fijos en el código. Python tiene varios tipos de l
# iterales, es decir, un literal puede ser un número
# por ejemplo, 123), # o una cadena (por ejemplo, "Yo soy un literal.")
# escribir una cadena

#Para codificar un apóstrofe o una comilla dentro de una cadena
#  se puede utilizar el carácter de escape, por ejemplo, 
# 'I\'m happy.', o abrir y cerrar la cadena utilizando un conjunto
#  de símbolos distintos al símbolo que se desea codificar, por ejemplo,
#  "I'm happy." para codificar un apóstrofe, y 'Él dijo "Python", no "typhoon"' 
#  para codificar comillas

print("Hola amigos")
#manera de como salir de las comillas dobles
print("Me gusta \"Este Helado\"")
print('Me gusta "El helado de chocolate"')
print('"Estoy"')
print('""aprendiendo""')
print('"""python"""')

# Demostrando la función chr()

print(chr(97))
print(chr(945))

# Demostrando la función ord ()

ch1 = 'a' 
ch2 = ' ' # espacio

print(ord(ch1))
print(ord(ch2))

# Indexando cadenas

exampleString = 'silly walks'

for ix in range(len(exampleString)):
    print(exampleString[ix], end=' ')

print()

# Rodajas o rebanadas

alpha = "abdefg"

print(alpha[1:3])
print(alpha[3:])
print(alpha[:3])
print(alpha[3:-2])
print(alpha[-3:4])
print(alpha[::2])
print(alpha[1::2])


## probando operador IN
alpfabeto = "abcdefghijklmnopqrstuvwxyz"

print("f" in alpfabeto)
print("F" in alpfabeto)
print("1" in alpfabeto)
print("ghi" in alpfabeto)
print("Xyz" in alpfabeto)

## probando operador  NOT IN
alfabeto = "abcdefghijklmnopqrstuvwxyz"

print("f" not in alfabeto)
print("F" not in alfabeto)
print("1" not in alfabeto)
print("ghi" not in alfabeto)
print("Xyz" not in alfabeto)

# manera de agrergar valores a una cadena
alfabeto = "bcdefghijklmnopqrstuvwxy"

alfabeto = "a" + alfabeto
alfabeto = alfabeto + "z"

print(alfabeto)

# Demonstrando min() - Ejemplo 1
print(min("aAbByYzZ"))


# Demonstrando min() - Examplos 2 y 3
t = 'Los Caballeros Que Dicen "¡Ni!"'
print('[' + min(t) + ']')

t = [0, 1, 2]
print(min(t))

# Demostrando max() - Ejemplo 1
print(max("aAbByYzZ"))


# Demonstrando max() - Examplos 2 y 3
t = 'Los Caballeros Que Dicen "¡Ni!"'
print('[' + max(t) + ']')

t = [0, 1, 2]
print(max(t))

# Demonstrando el método index()
print("aAbByYzZaA".index("b"))
print("aAbByYzZaA".index("Z"))
print("aAbByYzZaA".index("A"))

# Demostrando la función list()
print(list("abcabc"))

# Demostrando el método count()
print("abcabc".count("b"))
print('abcabc'.count("d"))


# Demostración del método capitalize()
print('aBcD'.capitalize())
print("Alpha".capitalize())
print('ALPHA'.capitalize())
print(' Alpha'.capitalize())
print('123'.capitalize())
print("αβγδ".capitalize())

# Demostración del método center()
print('[' + 'alfa'.center(10) + ']')
print('[' + 'Beta'.center(2) + ']')
print('[' + 'Beta'.center(4) + ']')
print('[' + 'Beta'.center(6) + ']')
print('[' + 'gamma'.center(20, '*') + ']')

# Demostración del método endswith()
if "epsilon".endswith("on"):
    print("si")
else:
    print("no")
    
t = "zeta"
print(t.endswith("a"))
print(t.endswith("A"))
print(t.endswith("et"))
print(t.endswith("eta"))

# Demostración del método find()
print("Eta".find("ta"))
print("Eta".find("mma"))
t = 'teta'
print(t.find('eta'))
print(t.find('et'))
print(t.find('te'))
print(t.find('ha'))
print('kappa'.find('a', 2))
txt = """A variation of the ordinary lorem ipsum
text has been used in typesetting since the 1960s 
or earlier, when it was popularized by advertisements 
for Letraset transfer sheets. It was introduced to 
the Information Age in the mid-1980s by the Aldus Corporation, 
which employed it in graphics and word-processing templates
for its desktop publishing program PageMaker (from Wikipedia)"""

fnd = txt.find('the')
while fnd != -1:
    print(fnd)
    fnd = txt.find('the', fnd + 1)

    # Demostración del método the isalnum()
print('lambda30'.isalnum())
print('lambda'.isalnum())
print('30'.isalnum())
print('@'.isalnum())
print('lambda_30'.isalnum())
print(''.isalnum())
t = 'Six lambdas'
print(t.isalnum())

t = 'ΑβΓδ'
print(t.isalnum())

t = '20E1'
print(t.isalnum())

# Ejemplo 1: Demostración del método isapha()
print("Moooo".isalpha())
print('Mu40'.isalpha())

# Ejemplo 2: Demostración del método isdigit()
    
print('2018'.isdigit())
print("Año2019".isdigit())

# Ejemplo 1: Demostración del método islower()
print("Moooo".islower())
print('moooo'.islower())

# Ejemplo 2: Demostración del método isspace()
print(' \n '.isspace())
print(" ".isspace())
print("mooo mooo mooo".isspace())

# Ejemplo 3: Demostración del método isupper() 
print("Moooo".isupper())
print('moooo'.isupper())
print('MOOOO'.isupper())

# Demostración del método join()
print(",".join(["omicron", "pi", "rho"]))

# Demostración del método the lstrip()
print("[" + " tau ".lstrip() + "]")
print("www.cisco.com".lstrip("w."))
print("pythoninstitute.org".lstrip(".org"))

# Demostración del método replace()
print("www.netacad.com".replace("netacad.com", "pythoninstitute.org"))
print("This is it!".replace("is", "are"))
print("Apple juice".replace("juice", ""))
print("This is it!".replace("is", "are", 1))
print("This is it!".replace("is", "are", 2))

# Demostración del método rfind()
print("tau tau tau".rfind("ta"))
print("tau tau tau".rfind("ta", 9))
print("tau tau tau".rfind("ta", 3, 9))  

# Demostración del método rstrip()
print("[" + " upsilon ".rstrip() + "]")
print("cisco.com".rstrip(".com"))

# Demostración del método split()
print("phi       chi\npsi".split())

# Demostración del método startswith()
print("omega".startswith("meg"))
print("omega".startswith("om"))

print()

# Demostración del método strip() 
print("[" + "   aleph   ".strip() + "]")

# Demostración del método swapcase()
print("Yo sé que no sé nada.".swapcase())

print()

# Demostración del método title()
print("Yo sé que no sé nada. Parte 1.".title())

print()

# Demostración del método upper()
print("Yo sé que no sé nada. Parte 2.".upper())

# Demostración de la función sorted()
firstGreek = ['omega', 'alfa', 'pi', 'gama']
firstGreek2 = sorted(firstGreek)

print(firstGreek)
print(firstGreek2)

print()

# Demostración del método sort()
secondGreek = ['omega', 'alfa', 'pi', 'gama']
print(secondGreek)

secondGreek.sort()
print(secondGreek)

# demostracion de ambos ordenamientos

thirdGreek = ['julio','camilo','andres','ana','william']
print(thirdGreek)
thirdGreek2 = sorted(thirdGreek)
thirdGreek.sort()
print(thirdGreek)
print(thirdGreek2)

# Cifrado César
text = input("Ingresa tu mensaje: ")
cifrado = ''
for char in text:
    if not char.isalpha():
        continue
    char = char.upper()
    code = ord(char) + 1
    if code > ord('Z'):
        code = ord('A')
    cifrado += chr(code)

print(cifrado)

# Cifrado César - descifrar un mensaje
cifrado = input('Ingresa tu criptograma: ')
text = ''
for char in cifrado:
    if not char.isalpha():
        continue
    char = char.upper()
    code = ord(char) - 1
    if code < ord('A'):
        code = ord('Z')
    text += chr(code)

print(text)

#Procesador de números

linea = input("Ingresa una línea de números, sepáralos con espacios: ")
strings = linea.split()
total = 0
try:
    for substr in strings:
        total += float(substr)
    print("El total es:", total)
except:
    print(substr, "no es un numero.")