"""Manejo de errores"""

"""
- Crear una función aplicado excepeciones donde el bloque del except
va a considerar a los errores entre cero y el tipo de error
- Los valores tienen qie ser ingresados por consola.
"""

"""
try:
    bloque de código 1
except ("exepcion 1", "exepcion 2", "exepcion 3")
    bloque de código 2
else:
    bloque de código 3
"""

"""
TypeError
ZeroDivisionError
IndexError
KeyError
FileNotFoundError
ImportError
OverFlowError
"""


def operacion(var_1, var_2):
    try:
        resultado_1 = var_1 / var_2
    except (ZeroDivisionError, TypeError):
        print("No se puede ejecutar la operación")
    else:
        print(f"El resultado de la division es: {resultado_1}")


operacion(50, "Python")
operacion(100, 0)
operacion(50, 50)

"""
def operaciones (a, b):
    try:
        pass
    except:
        pass
operaciones(50, 0)
operaciones(40, "Perú")
"""
