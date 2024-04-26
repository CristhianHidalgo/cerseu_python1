"""Programación orientada a objetos en Python"""
# Atributos

class Carro:
    #Atributos
    ruedas = 4

    #Constructor: Valores que van a tener por defecto mi clase que se le instancia en una variable

    def __init__(self, color, aceleracion):
        self.color = color
        self.aceleracion = aceleracion
        self.velocidad = 0

    #Métodos: Son las funciones de las clases

    def acelerar(self):
        self.velocidad = self.velocidad + self.aceleracion

    def frenar(self):
        velocidad = self.velocidad - self.aceleracion

        if velocidad < 0:
            velocidad = 0
        self.velocidad = velocidad

#Instanciamos nuestra clase
carro_1 = Carro("White", 70)
print (f"El color de mi primer carro es: {carro_1.color}")

carro_2 = Carro("Red", 90)
carro_2.marchas = 6
print(f"El número de marchas de mi segundo carro es {carro_2.marchas}")

"""IMPORTANTE
No se posbible llamar un atributo a una ...."""
print(carro_1.marchas)
