## Diccionarios
dict = {"gato" : "chat", "perro" : "chien", "caballo" : "cheval"}
numerosTelefono = {'jefe' : 5551234567, 'Suzy' : 22657854310}
diccionarioVacio = {}

print(dict)
print(numerosTelefono)
print(diccionarioVacio)

# obtener valores especificos
print(dict['gato'])
print(numerosTelefono['Suzy'])

### se emplea el metodo GET para obtener datos
polEspDict = {
    "kwiat" : "flor",
    "woda"  : "agua",
    "gleba" : "tierra"
    }

elemento2 = polEspDict.get("woda")
print(elemento2)    # salida: agua

## manera mas optima de encontrar valores especificos sin fallar en el intento
dict = {"gato" : "chat", "perro" : "chien", "caballo" : "cheval"}
words = ['gato', 'leon', 'caballo']

for word in words:
    if word in dict:
        print(word, "->", dict[word])
    else:
        print(word, "no está en el diccionario")

## retornar valores de manera ordenada con la palabra reservada KEYS()
dict = {"gato" : "chat", "perro" : "chien", "caballo" : "cheval"}

for key in dict.keys():
    print(key, "->", dict[key])

## retorna los valores de manera No ordenada con la palabra reservada. SORTED
dict = {"gato" : "chat", "perro" : "chien", "caballo" : "cheval"}

for key in sorted(dict.keys()):
    print(key, "->", dict[key])

## manera en que regresa una lista de tuplas para entregar a cada una con su valor
## con la palabra reservada .items
dict = {"gato" : "chat", "perro" : "chien", "caballo" : "cheval"}

for spanish, french in dict.items():
    print(spanish, "->", french)

#### ejemplo con items
colores = {
    "blanco" : (255, 255, 255),
    "gris"   : (128, 128, 128),
    "rojo"   : (255, 0, 0),
    "verde"  : (0, 128, 0)
    }

for col, rgb in colores.items():
    print(col, ":", rgb)


### otra manera de hacerlo es con la palabra reservada values(), pero esta solo regresa
### una lista de valores
dict = {"gato" : "chat", "perro" : "chien", "caballo" : "cheval"}

for french in dict.values():
    print(spanish, "->", french)

### modificar los valores de un diccionario
dict = {"gato" : "perro", "dog" : "chien", "caballo" : "cheval"}

dict['gato'] = 'minou'
print(dict)

### agregar valores al diccionario
dict = {"gato" : "chat", "perro" : "chien", "caballo" : "cheval"}

dict['cisne'] = 'cygne'
print(dict)

#### otra manera de asignar mas valores al diccionario
dict = {"gato" : "chat", "perro" : "chien", "caballo" : "cheval"}
dict.update({"pato" : "canard"})
print(dict)

##### eliminar valores de los diccionarios. El valor a eliminar se va con su correspondiente
dict = {"gato" : "chat", "perro" : "chien", "caballo" : "cheval"}

del dict['perro']
print(dict)

##### para eliminar el ultimo elemento del diccionario se usa la palabra reservada POPITEM
dict = {"gato" : "chat", "perro" : "chien", "caballo" : "cheval"}

dict.popitem()
print(dict)    

###### para eliminar los elementos del diccionario se emplea CLEAR()

polEspDict = {
    "zamek" : "castillo",
    "woda"  : "agua",
    "gleba" : "tierra"
    }

print(len(polEspDict))    # salida: 3
del polEspDict["zamek"]    # elimina un elemento
print(len(polEspDict))    # salida: 2

polEspDict.clear()   # elimina todos los elementos
print(len(polEspDict))    # salida: 0

del polEspDict    # elimina el diccionario

###### para copiar un diccionario emplea el metodo COPY()
polEspDict = {
    "zamek" : "castillo",
    "woda"  : "agua",
    "gleba" : "tierra"
    }

copyDict = polEspDict.copy()

##### ejemplo para copiar DICCIONARIOS
miDict = {"A":1, "B":2}
copyMiDict = miDict.copy()
miDict.clear()

print(copyMiDict)


#####Escribe un programa que "una" los dos diccionarios (d1 y d2) para crear uno nuevo (d3).
d1 = {'Adam Smith':'A', 'Judy Paxton':'B+'}
d2 = {'Mary Louis':'A', 'Patrick White':'C'}
d3 = {}

for elemento in (d1,d2):
    d3.update(elemento)
print(d3)

####### para darle valores a las claves
mitupla = ("España","Francia","Reino unido","Alemania")
midiccionario = {mitupla[0]:"Madrid", mitupla[1]:"Paris", mitupla[2]:"Londres", mitupla[3]:"Berlin"}
print(midiccionario)

##### ingresar tuplas dentro de un diccionario
midiccionario = {23:"jodan", "Nombre":"Michael","Equipo":"Chicago","Anillos":(1991,1992,1993,1996,1997,1998)}
print(midiccionario)

##### ingresar tuplas y diccionaros dentro de un diccionario
midiccionario = {23:"jodan", "Nombre":"Michael","Equipo":"Chicago","Anillos":{"Temporadas":(1991,1992,1993,1996,1997,1998)}}
print(midiccionario)