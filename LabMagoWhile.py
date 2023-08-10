numeroSecreto = 777
print(
"""
+==================================+
| Bienvenido a mi juego, muggle!   |
| Introduce un número entero       |
| y adivina qué número he          |
| elegido para ti.                 |
| Entonces,                        |
| ¿Cuál es el número secreto?      |
+==================================+
""")
numeroSecreto = int (input("introduzca el numero secreto: "))
while numeroSecreto != 777:
    print ("Ja Ja estas atrapado en mi ciclo")
    numeroSecreto = int(input("introduzca el numero secreto: "))

    if numeroSecreto == 777:
        print ("bien hecho, muggle eres libre")
    
