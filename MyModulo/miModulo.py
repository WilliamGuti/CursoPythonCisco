#! /usr/bin/env python3  #dicha linea indica el SO como ejecutar el contenido del archivo para Unix o MacOs

__cont = 0 

def sum1(list):
    global __cont
    __cont += 1
    sum = 0
    for el in list:
        sum += el
    return sum

def prod1(list):
    global __cont
    __cont += 1
    prod = 1
    for el in list:
        prod *= el
    return prod

if __name__ =='__main__':
    print('I prefer to be a module, but i can do some test for you')
    l = [i + 1 for i in range(5)]
    print(sum1(1) == 15)
    print(prod1(1) == 120)
# else:
#     print('I like to be a Module')