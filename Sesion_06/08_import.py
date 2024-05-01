from func import funciones

var_1 = int(input("Ingrese el valor de la variable 1: "))
var_2 = int(input("Ingrese el valor de la variable 2: "))

sum = funciones.suma(var_1, var_2)
print(f"El resultado de la suma es: {sum}")

rest = funciones.resta(var_1, var_2)
print(f"El resultado de la resta es: {rest}")

mult = funciones.multiplicacion(var_1, var_2)
print(f"El resultado de la multiplicacion es: {mult}")