"""
Requisitos:

- Dentro de una empresa se va a solicitar pedir nombre y apellido del empleado.
- Distrito de residencia
- Sueldo y el calculo del bono final del año, que será el triple de sueldo mensual menos el 10 por ciento del sueldo
- Todos estos datos van a estar asignados en una lista
- Por asignación múltiple de variables, asignar los valores de esta lista a 3 nuevas variables
- Mostar por la terminar el mensaje del 'nombre', 'apellido' recibira 'bono' soles de bono de fin de año
"""

nombre_apellido = input("Ingrese su nombre y apellido: ")
distrito = input("Ingrese su distrito de residencia: ")
sueldo = int(input("Ingrese su sueldo: "))

bono = 3 * sueldo - sueldo * 0.1

datos = [nombre_apellido, distrito, sueldo]

nombre_apellido2, distrito2, sueldo2 = datos

print(f"{nombre_apellido2} recibira {bono} soles de bono de fin de año")