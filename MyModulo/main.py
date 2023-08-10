from sys import path
path.append('C:\\Users\\William\\Desktop\\CursoPythonCisco\\MyModulo\\modulos')
import miModulo
zeros = [0 for i in range(5)]
unos = [1 for i in range(5)]
print(miModulo.sum1(zeros))
print(miModulo.prod1(unos))