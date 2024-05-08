"""Manejo de archivos"""

def fileManipulation(dir, mode):
    try:
        file = open(dir, mode)
        print(file.read())
        file.close()
        return file
    except OSError as err:
        print(f"Error de lectura :{err}")

dir_file = "../Sesion_07/my_files/file_4.txt"
print("Lectura de archivo")

fileManipulation(dir_file, "r")