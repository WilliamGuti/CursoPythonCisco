from gc import callbacks
from opcode import hascompare
from tkinter.tix import Tree
from traceback import print_tb


class vehiculos(): #superclase
    def __init__(self,marca,modelo): #constructor
        #atributos
        self.marca = marca
        self.modelo = modelo
        self.enMarcha = False
        self.acelera = False
        self.frena = False
    #metodos
    def arrancar(self):
        self.enMarcha = True

    def acelerar(self):
        self.acelera = True
    
    def frenar(self):
        self.frena = True

    def estado(self):
        print('Marca:', self.marca ,'\nmodelo:', self.modelo,'\nen marcha:',
            self.enMarcha, '\nAcelerando: ', self.acelera,'\nFrenando: ',self.frena)


class furgoneta(vehiculos):
    
    def carga(self,cargar):
        self.cargado = cargar
        if(self.cargado):
            return 'La furgoneta esta cargada'
        else:
            return 'La furgoneta no esta cargada'

class moto(vehiculos): #subclase que hereda
    hcaballito = ''
    def caballito(self):
        self.hcaballito = 'Voy haciendo el caballito'
    def estado(self):
        print('Marca:', self.marca ,'\nmodelo:', self.modelo,'\nen marcha:',
            self.enMarcha, '\nAcelerando: ', self.acelera,'\nFrenando: ',self.frena,
            '\n',self.hcaballito)


class VElectricos(vehiculos):
    def __init__(self,marca,modelo):
        super().__init__(marca,modelo)
        self.autonomia = 100
    
    def cargarEnergia(self):
        self.cargando = True

class bicicletaElectrica(VElectricos,vehiculos):
    
    pass



print('............Instanciacion de moto............')
miMoto = moto('honda','CB') 
miMoto.arrancar()
miMoto.acelerar()
miMoto.caballito()
miMoto.estado()
print('............Instanciacion de furgoneta............')
miFurgoneta = furgoneta('Jepp','Rubicon')
miFurgoneta.arrancar()
miFurgoneta.estado()
print(miFurgoneta.carga(True))
print('............Instanciacion de vehiculos electricos............')
miBici = bicicletaElectrica('Electra','XRl8')
