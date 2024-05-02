"""POO Python"""
#Polimorfismo
class Perro():
    def sonido(self):
        print("Guau")

class Gato():
    def sonido(self):
        print("Miauuu")

class Vaca():
    def sonido(self):
        print("Muuu")

gato = Gato()
perro = Perro()
vaca = Vaca()

lista_animales = [perro, gato, vaca]

def canto(lista):
    for animal in lista:
        animal.sonido()

canto(lista_animales)

