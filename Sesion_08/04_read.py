"""Manejo de archivos"""

"""Apertura y lectura de archivos"""

"""
    r: Abre el archivo en modo lectura
"""

file = open("my_files/file.txt", "r")

"""
    read(): Nos permite leer el contenido de un archivo
"""

print(f"El contenido de nuestro archivo 'file' es: {file.read()}")

"""Cierre de archivos"""
file.close()