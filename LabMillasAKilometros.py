# Definimos las variables
kilometros = 12.25
millas = 7.38
# Hacemos las operaciones
millas_a_kilometros = millas / 0.62137
kilometros_a_millas = kilometros * 0.62137
# imprimimos
print(millas, " millas son ", round(millas_a_kilometros, 2), " kilómetros ")
print(kilometros, " kilómetros son ", round(kilometros_a_millas, 2), " millas ")
# Round se utiliza para redondear valores flotantes con cierta cantidad de decimales
