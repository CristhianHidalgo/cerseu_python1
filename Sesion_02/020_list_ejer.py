
"""Listas en Python"""

"""Requisitos

- Crear dos listas vacias inicialmente
- Agregar luego los datos de nombre, edad, profesión para ambos usando append
- Sumar ambdas listas y mostrar el resutlado en consola
- Mostrar de manera inversa la suma de ambas listas
- Actualizar la nueva lista eliminando las edades de ambas personas con remove
"""

persona1 = []
persona2 = []

persona1.append("Juan")
persona1.append(30)
persona1.append("Arquitecto")

persona2.append("María")
persona2.append(40)
persona2.append("Profesora")

suma_persona = persona1 + persona2
print("El resultado de la suma de ambas listas es: {}".format(suma_persona))

suma_persona.reverse()
print("La inversa de la suma de las listas es: {}".format(suma_persona))

suma_persona.remove(30)
suma_persona.remove(40)

print("La suma de la lista actualizada es: {}".format(suma_persona))