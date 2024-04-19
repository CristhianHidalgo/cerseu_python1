"""Listas en Python"""

"""Listas (del): Eliminamos un valor indicando el índice del valor en una lista"""

paises = []
paises.append("Perú")
paises.append("Brasil")
paises.append("Canadá")
paises.append("Chile")
paises.append("España")
paises.append("Francia")

print("Los valores de mi lista son: {}".format(paises))

del paises[2]

print("Los valores de mi nueva lista es: {}".format(paises))


