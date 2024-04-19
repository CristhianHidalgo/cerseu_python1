
""""Diccionarios en Python"""

"""del: elimina un key y su calor correspondiente en el diccionario"""

var_1 = {"nombre": "Margaret", "edad": 27, "promedio": 16}

"""Para eliminar valore de nuestro diccionario usamos a del adelante de la variable"""

del var_1["edad"]
del var_1["promedio"]

print(f"El diccionario actualizado tiene los siguientes valores: {var_1}")