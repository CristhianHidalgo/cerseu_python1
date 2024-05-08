"""Gestión de excepciones"""

"""Estructura y uso"""
"""
try:
    bloque de código 1
except 'excepcion 1':
    bloque de código 2
except 'excepcion 2':
    bloque de cógigo 3
else:
    bloque de código 4
"""
def division(a, b):
    try:
        resultado = a/b
    except ZeroDivisionError:
        print("¡No se puede dividir entre cero!")
    else:
        print("El resultado es: ", resultado)


division(40, 0)
division(190, 5)