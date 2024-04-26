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


carro_1 = Carro("Azul", 100)

print(f"La velocidad inicial de mi carro 1 es: {carro_1.velocidad}")

carro_1.acelerar()
carro_1.acelerar()
carro_1.acelerar()
carro_1.acelerar()

print(f"La nueva velocidad de mi carro 1 es: {carro_1.velocidad}")

carro_1.frenar()

print(f"La velocidad de mi carro 1 es: {carro_1.velocidad}")
