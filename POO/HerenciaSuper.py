from traceback import print_tb


class Persona():
    def __init__(self, nombre, edad, ciudad):
        self.nombre = nombre
        self.edad = edad
        self.ciudad = ciudad
    def descripcion(self):
        print('Nombre:',self.nombre,'\nEdad:',self.edad
            ,'\nCiudad:',self.ciudad)

class Empleado(Persona):
    def __init__(self, salario, antiguedad, nombreEmpleado, edadEmpleado, ciudadEmpleado):
        super().__init__(nombreEmpleado, edadEmpleado ,ciudadEmpleado)
        self.salario = salario
        self.antiguedad = antiguedad
    def descripcion(self):
        super().descripcion()
        print('El salario es:',self.salario,'\nAntiguedad:',self.antiguedad)
        
persona = Empleado(1000,4,'William',25,'Bogota')

persona.descripcion()

print(isinstance(persona,Empleado))