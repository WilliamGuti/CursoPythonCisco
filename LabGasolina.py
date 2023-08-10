# Tu tarea es escribir un par de funciones que conviertan l/100km a mpg(milas por galón), y viceversa.

# datos de interes:
KilometrosPorMilla = 1.609344 #1 millas en metros
LitroPorGalón = 3.785411784 #1 galon en litros

def l100kmtompg(liters):
    resultado = (100*LitroPorGalón)/(KilometrosPorMilla*liters)
    return resultado

def mpgtol100km(miles):
    result = (100*LitroPorGalón)/(miles*KilometrosPorMilla)
    return (result)

print(l100kmtompg(3.9))
print(l100kmtompg(7.5))
print(l100kmtompg(10.))

print(mpgtol100km(60.3))
print(mpgtol100km(31.4))
print(mpgtol100km(23.5))
