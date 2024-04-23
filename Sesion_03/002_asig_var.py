""""Entradas y Salidas"""
"""Referencia a dos o más variables"""

var_1 = input("\nIngrese nombre de usuario: ")
var_2 = input("Ingrese su nombre: ")
var_3 = int(input("Ingrese su edad: "))

"""usuario = var_1
nombre = var_2
edad = var_3"""

usuario, nombre, edad = var_1, var_2, var_3

print(f"\nSu nombre de usuario es {usuario} y tiene {edad} años")