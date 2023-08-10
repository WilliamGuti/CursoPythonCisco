# un ejemplo de como utilizar variables dentro de una clase, para poder 
# ejecutarlas dentro de un constructor o en otro metodo
class ClaseEjemplo:
    contador = 0
    def __init__(self, val = 1):
        self.__primera = val
        ClaseEjemplo.contador += 1

objetoEjemplo1 = ClaseEjemplo()
objetoEjemplo2 = ClaseEjemplo(2)
objetoEjemplo3 = ClaseEjemplo(4)

print(objetoEjemplo1.__dict__, objetoEjemplo1.contador)
print(objetoEjemplo2.__dict__, objetoEjemplo2.contador)
print(objetoEjemplo3.__dict__, objetoEjemplo3.contador)

# la palabra __dict__ nos ayuda a presentar los resultados en forma
# de diccionario con su respectivo valor, el cual va en incremento
# por el contador que se esta realizando en el constructor

######################################
class ClaseEjemplo:
    __contador = 0
    def __init__(self, val = 1):
        self.__primera = val
        ClaseEjemplo.__contador += 1

objetoEjemplo1 = ClaseEjemplo()
objetoEjemplo2 = ClaseEjemplo(2)
objetoEjemplo3 = ClaseEjemplo(4)
    
print(objetoEjemplo1.__dict__, objetoEjemplo1._ClaseEjemplo__contador)
print(objetoEjemplo2.__dict__, objetoEjemplo2._ClaseEjemplo__contador)
print(objetoEjemplo3.__dict__, objetoEjemplo3._ClaseEjemplo__contador)


######################################
# la manera de encontrar variables no existentes en las clases, se puede hacer de dos formas
# con un TRY-EXCEPT o con una funcion de python llamanda HASATTR la cual permite veriificar si es cierto o no
    # con TRY-EXCEPT
class ClaseEjemplo:
    def __init__(self, val):
        if val % 2 != 0:
            self.a = 1
        else:
            self.b = 1

objetoEjemplo = ClaseEjemplo(1)
print(objetoEjemplo.a)

try:
    print(objetoEjemplo.b)
except AttributeError:
    pass
    # con HASSATTR
class ClaseEjemplo:
    def __init__(self, val):
        if val % 2 != 0:
            self.a = 1
        else:
            self.b = 1

objetoEjemplo = ClaseEjemplo(1)
print(objetoEjemplo.a)

if hasattr(objetoEjemplo, 'b'):
    print(objetoEjemplo.b)

# otra forma de averiguarlo directamente
class ClaseEjemplo:
    attr = 1

print(hasattr(ClaseEjemplo, 'attr'))
print(hasattr(ClaseEjemplo, 'prop'))

class ClaseEjemplo:
    a = 1
    def __init__(self):
        self.b = 2

objetoEjemplo = ClaseEjemplo()

print(hasattr(objetoEjemplo, 'b'))
print(hasattr(objetoEjemplo, 'a'))
print(hasattr(ClaseEjemplo, 'b'))
print(hasattr(ClaseEjemplo, 'a'))