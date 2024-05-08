"""Decoradores en Python"""

"""Creación interna de la función decoradora"""

def funcionA(funcionB):
    def funcionC(*args, **kwargs):
        print("1. Antes de ejecutar la función que ha sido decorada")
        resultado = funcionB(*args, **kwargs)
        print("2. Después de ejecutar la función que ha sido decorada")
        return resultado
    return funcionC

@funcionA
def saludar(nombre, apellido, edad, **kwargs):
    print(f"Hola {nombre} {apellido}, usted tiene {edad} años")
    for key, value in kwargs.items():
        print(f"{key} = {value}")

nombre = input("Ingrese su nombre porfavor: ")
apellido = input("Ingrese su apellido porfavor: ")
edad = input("Ingrese su edad porfavor: ")

saludar(nombre, apellido, edad, ciudad1="Piura", ciudad2="Arequipa", ciudad3="San Francisco")

