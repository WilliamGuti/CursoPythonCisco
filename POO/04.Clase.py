# la manera en que podemos reutilizar los metodos de una clase, para poder implementarlas en varios objetos.
# De esta forma podemos hacer que el codigo pueda ser mas corto. pero creando mas objetos al vez que utilicen
# las metodos de la misma clase
class Pila:
    def __init__(self):
        self.__listaPila = []

    def push(self, val):
        self.__listaPila.append(val)

    def pop(self):
        val = self.__listaPila[-1]
        del self.__listaPila[-1]
        return val


objetoPila1 = Pila()
objetoPila2 = Pila()

objetoPila1.push(3)
objetoPila2.push(objetoPila1.pop())

print(objetoPila2.pop())

## otro ejemplo seria, para la manipulacion de otros objetos
class Pila:
    def __init__(self):
        self.__listaPila = []

    def push(self, val):
        self.__listaPila.append(val)

    def pop(self):
        val = self.__listaPila[-1]
        del self.__listaPila[-1]
        return val    
    
pequeñaPila = Pila()
otraPila = Pila()
graciosaPila = Pila()

pequeñaPila.push(1)
otraPila.push(pequeñaPila.pop() + 1)
graciosaPila.push(otraPila.pop() - 2)

print(graciosaPila.pop())