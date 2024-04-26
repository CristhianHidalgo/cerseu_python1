"""Programación fundamental en Python"""

""""
Requisitos:
- Un usuario ingresará 2 números por consola
- En una función obtener si el segundo número ingresado es múltiplo del primero o viceversa
- Retornar quién fue múltiple de quien
"""

a = int(input("Ingrese el primer número: "))
b = int(input("Ingrese el segundo número: "))

def multiplo(a, b):
    if a % b == 0:
        print(f"{a} es multiplo de {b}")
    elif b % a == 0:
        print(f"{b} es multiplo de {a}")
    else:
        print("Los números no son múltiplos")

multiplo(a,b)