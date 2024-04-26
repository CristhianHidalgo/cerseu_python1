"""Programación fundamental en Python"""

""""
Requisitos: 
- Solicitar al usuario 4 números por consola
- Crear una función que devuelve cuál es el número mayor de los 4 ingresados por el usuario
- Finalmente elevar al cubo el resutlado y mostrarlo por consola
"""

a = int(input("Ingresa el primer número: "))
b = int(input("Ingresa el segundo número: "))
c = int(input("Ingresa el tercer número: "))
d = int(input("Ingresa el cuarto número: "))

def mayor(a, b, c, d):
    return max(a, b, c, d)

print(f"El número mayor es: {mayor(a, b, c, d)}")

cubo = mayor(a, b, c, d) ** 3
print(f"El cubo del número mayor es: {cubo}")

def mayor_1(a, b, c, d):
    if a>b & a>c & a>d:
        return a
    if b>a & b>c & b>d:
        return b


