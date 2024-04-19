"""Uso del flujo condicional: if"""

var_1 = int(input("Ingrese su primer dato numerico: "))
var_2 = int(input("Ingrese su segundo dato numerico: "))

if var_1 > var_2:
    print("El primer dato es mayor que el segundo")

elif var_1 == var_2:
    print("Los valores ingresados son iguales")

else:
    print("El primer dato es menor que el segundo")
