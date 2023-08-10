# lee la variable

año = int(input("Introduzca un año:"))

#condicionales

if año <= 1582:
    print("no dentro del periodo del calendario gregoriano")
elif año % 4 != 0:
    print("año comun")
elif año % 4==0 and año % 100!=0:
    print("año bisiesto")
elif año % 4==0 and año % 100==0 and año % 400!=0:
    print("año comun")
else:
    print("año bisiesto")  