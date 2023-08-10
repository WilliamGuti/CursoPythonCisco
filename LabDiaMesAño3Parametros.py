# Tu tarea es escribir y probar una función que toma tres argumentos (un año, un mes y un día del mes)
# y devuelve el día correspondiente del año, o devuelve None si cualquiera de los argumentos no es válido.

def isYearLeap(year):
	if year >= 1582:
		if year % 4 != 0:
			return False
		elif year % 100 != 0:
			return True
		elif year % 400 != 0:
			return False
		else:
			return True

diasMeses = [31,28,31,30,31,30,31,31,30,31,30,31]

def daysInMonth(year, month):
	if month == 1 and isYearLeap(year):
		return 29
	else:
		return diasMeses[month]


def dayOfYear(year, month, day):
    contador = 0
    aux = 0
    for i in range(month):
        aux = daysInMonth(year,i) 
        if i == (month - 1):
            contador += day
        else:
            contador += aux
    return contador

print(dayOfYear(2000, 12, 31))