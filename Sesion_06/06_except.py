"""Gestión de operaciones"""

"""
    Crear una función aplicando excepeciones donde no se puede
    realizar una suma de diferentes tipos de datos
"""
def operaciones(a, b):
    try:
        resultado = a/b
    except TypeError:
        print("No se puede sumar un str con un int")
    except ZeroDivisionError:
        print("No se puede dividir entre cero")
        resultado = 0
        print(f"Resultado: {resultado}")
    else:
        print(resultado)

#operaciones(40, "Python")
#operaciones(100, 500)
operaciones(500, 0)