"""
Programación orientada a objetos en Python

Requerimientos:
- Clear clase alumno
- Debe tener un atrivuto de nacionalidad con valor Peruana
- Crear un método que indicará el promedio del alumno
- Crear un método que indicará si el alumno está aprobado(>=11) o no de acuerdo al promedio
- Tendrá 3 notas, la nota inicial será de 0 para todos
- Obtener el nombre y distrito del residente
"""

class Alumno:
    def __init__(self, nombre, distrito):
        self.nombre = nombre
        self.distrito = distrito
        self.nacionalidad = "Peruana"
        self.nota_1 = 0
        self.promedio = 0
        self.aprobado = False
        self.nota_2 = 0
        self.nota_3 = 0

    def promedio_nota(self):
        self.nota_2 = int(input("Ingrese la nota 2: "))
        self.nota_3 = int(input("Ingrese la nota 3: "))
        self.promedio = round(self.nota_1 + self.nota_2 + self.nota_3)/3
        return self.promedio
    def aprobado_nota(self):
        if self.promedio >= 11:
            print("Alumno aprobado")
        else:
            print("Alumno deaaprobado")

alumno_1 = Alumno("Carlos", "Sullana")
alumno_1.promedio_nota()
print(alumno_1.promedio)

alumno_1.aprobado_nota()
