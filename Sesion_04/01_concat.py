"""Usando las propiedades de cadenas de string"""

"""Concatenación"""

nombre = input("Ingrese su nombre: ")
apellido = input("Ingrese su apellido: ")

nombre_completo = "El nombre completo del usuario es: " + nombre + " " + apellido
print(nombre_completo)

nombre_completo_2 = f"El nombre completo del usuario es: {nombre} {apellido}"
print(nombre_completo_2)