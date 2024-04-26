"""Programación fundamental en Python"""


def multiplica(a, b, c=100):
    return a * b * c

print(f"El resultado de mi función es: {multiplica(40, 50)}")

#Es correcto usar la función cambiando el valor de mi parámetro
print(f"El resultado de mi función es: {multiplica(40, 2, 500)}")