# la manera de entrar a verificar la informacion de una propiedad que esta creada dentro de un objeto CONSTRUCTOR
# es de la siguiente manera
class Pila:
    def __init__(self):
        self.listaPila = []

objetoPila = Pila()
print(len(objetoPila.listaPila))

# la manera para ocultar los componentes de un objeto es de la siguiente manera
class Pila:
    def __init__(self):
        self.listaPila = []

objetoPila = Pila()
print(len(objetoPila.__listaPila))
# esto hace que se lance una excepcion, ya que solo se pueden acceder a los datos, desde la clase 