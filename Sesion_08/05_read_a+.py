"""Manejo de archivos"""

tecnologias_backend = ["\nPython", "Java", "Node JS", "Ruby"]
tecnologias_frontend = ["\nAngular", "React JS", "JavaScript", "Boostrap"]
base_datos = ["\nMySQL", "PostgreSQL", "DYNAMOb"]

"""
    a+: Permite escribir varías lineas en nuestro archivo
    a+: Escrbie nuevas lineas de texto sin sobreescribir el contenido del archivo
"""
file = open("my_files/file_2.txt", "a+")
#file.writelines(tecnologias_backend)
#file.writelines(tecnologias_frontend)
#file.writelines(base_datos)

file = open("my_files/file_2.txt", "r")
print(file.read())

"""Cierre de archivos"""
file.close()


