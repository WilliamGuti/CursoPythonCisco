class coche():
    def desplazamiento(self):
        print('Me desplazo utilizando cuatro ruedas')

class moto():
    def desplazamiento(self):
        print('Me desplazo utilizando dos ruedas')

class camion():
    def desplazamiento(self):
        print('Me desplazo utilizando seis ruedas')

# crear las instancias
# miVehiculo = moto()
# miVehiculo.desplazamiento()
# miVehiculo2 = coche()
# miVehiculo2.desplazamiento()
# miVehiculo3 = camion()
# miVehiculo3.desplazamiento()

# creamos un metodo para presindir de todo
def desplazamientoVehiculo(vehiculo):
    vehiculo.desplazamiento()
salir = ''

while salir != 'n':
    v = input('Ingresa un vehiculo: ')
    if v == 'moto':
        miVehiculo = moto()
        desplazamientoVehiculo(miVehiculo)
    elif v == 'coche':
        miVehiculo = coche()
        desplazamientoVehiculo(miVehiculo)
    elif v == 'camion':
        miVehiculo = camion()
        desplazamientoVehiculo(miVehiculo)
    else:
        print('Su vehiculo no se encuentra disponible')
    salir = input('Desea continuar? S/N ')
print('Has salido!')
