"""Usando las propiedades de cadenas o string"""

"""
Requisitos: 

- Ingresar tu nombre y apellido por consola (cada valor tiene que estar en una varibales distinta)
- Concatenar ambos valores en una sola variable
- Obtener y mostrar el tamaño el nombre completo
- Imprimir el resultado final todo en mayúscula
- Indicar mediante condicionales si el tamaño del nombre es mayor o no al del apellido (ingresar solo para este caso el apellido paterno)
"""

nombre = input("Ingresa tu nombre: ")
apellido = input("Ingresa tu apellido: ")

nombre_completo = nombre + " " + apellido

print(f"El tamaño del nombre completo es: {len(nombre_completo)}")
print(f"El nombre completo en mayúscula es: {nombre_completo.upper()}")

if len(nombre) > len(apellido):
    print("El tamaño del nombre es mayor al del apellido")
else:
    print("El tamaño del nombre es menor al del apellido")