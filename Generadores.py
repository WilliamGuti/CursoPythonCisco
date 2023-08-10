import re


def generaPares(limite):
    num = 1
   
    while num < limite:
        yield num*2
        num +=1

devuelvePares = generaPares(10)

print(next(devuelvePares)) # estado de suspencion
print('Aqui podria ir mas codigo...')
print(next(devuelvePares)) # estado de suspencion
print('Aqui podria ir mas codigo...')
print(next(devuelvePares)) # estado de suspencion