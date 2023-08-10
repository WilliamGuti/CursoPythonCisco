# de esta manera se puede empezar a crear una pila, con los valores necesarios en una lista
# con las funciones PUSH  y POP, podremos agregar y quitar valores de la lista
class Pila:
    def __init__(self):
        self.__listaPila = []

    def push(self, val):
        self.__listaPila.append(val)
        
    def pop(self):
        val = self.__listaPila[-1]
        del self.__listaPila[-1]
        return val


objetoPila = Pila()

objetoPila.push(3)
objetoPila.push(2)
objetoPila.push(1)



print(objetoPila.pop())
print(objetoPila.pop())
print(objetoPila.pop())