"""Manejo de archivos"""
"""Escritura y lectura de archivos"""

"""
    w: Abre el archivo para poder escribir sobre él
"""

file = open("my_files/file.txt", "w")

file.write("\n-Lenguaje multiplataforma")
file.write("\n-Basado en POO")
file.write("\n-Python es un lenguaje intuitivo")

file = open("my_files/file.txt", "r")
print (f"Nuestro archivo file_2.txt tiene el siguiente contenido: {file.read()}")

"""Cierre de archivo"""
file.close()