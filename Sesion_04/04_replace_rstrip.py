"""Usando las propiedades de cadenas o string"""

# Replace

cadena = ("Conexión a Base de Datos "
          "con Python")

cadena_2 = cadena.replace(cadena[0:6], "ppppp")
print(f"Cadena con reemplazo, tiene el siguiente "
      f"valor actualizado: {cadena_2}")

# Eliminación de espacios en blanco de mi cadena (después)
cadena_3 = "Conexión a Base de Datos con Python              "
cadena_4 = cadena_3.rstrip()
print(len(cadena_3))
print(f"Mi cadena actualizada sin espacios "
      f"en blanco es la siguiente: {len(cadena_4)}")
