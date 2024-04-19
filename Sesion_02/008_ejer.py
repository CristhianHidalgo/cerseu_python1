"""

Crear 3 variables: nombre, edad, país de residencia y distrito

requisitos:
- Nombre: string, edad: int, país de residencia: string, distrito: string
- Concatenar estos datos e indicar una oración como la siguiente
José tiene X años, es del distrito de "distrito" y viene de "país de residencia"
- Obtener el módulo de su edad al usarlo con el número 5, mostrar el módulo
"""
nombre = "Cristhian"
edad = 21
pais = "Perú"
distrito = "Sullana"

print("{} tiene {} años, es del distrito de {} y viene de {}.".format(nombre, edad, distrito, pais))

modulo = edad % 5
print(f"El modulo entre la edad y 5 es: {modulo}")
