from sys import set_coroutine_origin_tracking_depth
from setuptools import setup
setup(
    name = 'PaqueteCalculosBasicos',
    version='1.0',
    description='Sirve para hacer operaciones basicas de suma, resta, multiplicacion, division, potencia y redondeo',
    author='William',
    author_email='wgutierrezrobayo@gmail.com',
    packages= ['paqueteComplemento','paqueteComplemento.operacionesBasicas']
)

