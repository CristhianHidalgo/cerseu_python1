"""Manejo de errores"""

"""
- Crear una función aplicado excepeciones donde el bloque del except
va a considerar a los errores entre cero y el tipo de error
- Los valores tienen qie ser ingresados por consola. 
"""

"""
"""

def operacion():
    var_1 = int(input("Ingrese el primer valor: "))
    var_2 = int(input("Ingrese el segundo valor: "))
    try:
        resultado_1 = var_1 / var_2
    except (ZeroDivisionError, TypeError):
        print("No se puede ejecutar la operación")
    else:
        print(f"El resultado de la division es: {resultado_1}")

operacion()