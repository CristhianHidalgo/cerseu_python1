"""Uso del flujo condicional: 'if'"""
"""if ternario"""


"""
Requisitos:
- Ingresar por teclado el sueldo de un empleado
- Si el sueldo es mayor a 3000, imprimir "Su sueldo no tiene notificación"
- Casdo contrario: "Su suelto tiene bonificación este año"

"""

sueldo = int(input("Ingrese su sueldo del empleado: "))

bonificacion = "Su sueldo no tiene bonificacion" if sueldo > 3000 else "Su sueldo tiene bonificación este año"

print(bonificacion)