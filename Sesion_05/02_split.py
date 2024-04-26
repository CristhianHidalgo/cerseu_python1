"""Usando las propuedades de cadenas o string"""

""""Métodos de string"""

cadena = "Python para la predicción de fraude bancario o de préstamos"

#cadena_sin_espacio = cadena.split(sep="a")
cadena_sin_espacio = cadena.split()

print(f"Cadena separada por espacios en blanco dentro del string: {cadena_sin_espacio}")

for palabra in cadena_sin_espacio:
    print(palabra)