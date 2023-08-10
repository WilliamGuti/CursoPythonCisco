# podemos invocar otros metodos desde dentro de la clase
class conClase():
    def otro(self):
        print("otro")

    def metodo(self):
        print("método")
        self.otro()

obj = conClase()
obj.metodo()

# metodo Constructor
class conClase():
    def __init__(self, valor):
        self.var = valor
objClase = conClase('objeto')
print(objClase.var)

# se puede agregar a varios objetos
class conClase:
    def __init__(self, valor = None):
        self.var = valor

obj1 = conClase("objeto")
obj2 = conClase()

print(obj1.var)
print(obj2.var)

# una manera de poder ocultar algunos valores de los metodos es con  __ seguido de su nombre
# ejemplo
class conClase:
    def visible(self):
        print("visible")
    
    def __oculto(self):
        print("oculto")

obj = conClase()
obj.visible()

try:
    obj.__oculto()
except:
    print("fallido")

obj._conClase__oculto()

## __name__
class conClase:
    pass

print(conClase.__name__)
obj = conClase()
print(type(obj).__name__)

## __modulo__
class conClase:
    pass

print(conClase.__module__)
obj = conClase()
print(obj.__module__)