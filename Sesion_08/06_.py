"""Manejo de archivos"""

tecnologias_backend = ["\nPython", "Java", "Node JS", "Ruby"]

file = open("../Sesion_07/my_files/file_4.txt", "a+")

file.writelines(tecnologias_backend)

file = open("../Sesion_07/my_files/file_4.txt", "r")

tecnologia = input("Ingrese la tecnología a buscar: ")

for newLine in file:
    #print(newLine)
    if tecnologia in newLine:
        print(f"Tiene en su lista a {tecnologia}")

"""Cierre de archivo"""
file.close()