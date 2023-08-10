from msilib.schema import SelfReg


class Coche(): # definimos la clase

    def __init__(self): # creamos el constructor
        # Definimos los atributos
        self.__largoChasis = 250
        self.__anchoChasis = 120
        self.__ruedas = 4
        self.__enMarcha = False
    # definimimos los metodos
    def arrancar(self,arrancamos):
        self.__enMarcha = arrancamos
        if (self.__enMarcha):
            chequeo = self.__chequeoInterno()
        if (self.__enMarcha and chequeo):
            return 'EL coche esta en marcha'
        elif(self.__enMarcha and chequeo == False):
            return 'Algo ha ido mal en el chequeo. No podemos arrancar'
        else:
            return 'El coche esta parado'
    def estado(self):
        print('El coche tiene: ',self.__ruedas,'Ruedas. un ancho de: ', self.__anchoChasis,'y un largo de',
        self.__largoChasis)

    def __chequeoInterno(self):
        print('Realizando chequeo interno!')

        self.gasolina = 'ok'
        self.aceite = 'ok'
        self.puertas = 'cerradas'

        if (self.gasolina == 'ok' and self.aceite == 'ok' and self.puertas == 'cerradas'):
            return True
        else:
            return False

# imprimimos los resultados
miCoche = Coche() # instanciamos la clase

print(miCoche.arrancar(True))
miCoche.estado()

print('.......... a continuacion creamos el segundo objeto.........')

miCoche2 = Coche() # instanciamos la clase

print(miCoche2.arrancar(False))
miCoche2.estado()

