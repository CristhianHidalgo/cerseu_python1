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


#Aplicamos Herencia
#Creamos nuesta clase hija

class CarroVolador(Carro):
    ruedad = 6

    def __init__(self, color, aceleracion, estadoVolando = False):
        super().__init__(color, aceleracion)
        self.estadoVolando = estadoVolando

    def vuela(self):
        self.estadoVolando = True

    def aterriza(self):
        self.estadoVolando = False

carro_1 = Carro("Rojo", 50)
carro_volador = CarroVolador("Azul", 70)

print(f"El color del carro volador es: {carro_volador.color}")
print(f"El estado inicial del carro volador es: {carro_volador.aceleracion}")

carro_volador.vuela()
carro_volador.acelerar()
carro_volador.acelerar()

print(f"La velcoidad inicial del carro volador es: {carro_volador.velocidad}")

"""Esto no puede suceder, porque la herencia es solo sobre la clase HIJA"""
#print(f"El estado de vuelvo de mi primer carro es: {carro1.vuela()}")

"""Esto tampoco puede suceder porque es función, más no atributo, sería con carro_volador.estadoVolando"""
#print(f"El estado de vuelvo de mi primer carro es: {carro_volador.vuela()}")