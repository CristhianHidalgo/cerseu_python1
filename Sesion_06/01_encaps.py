"""POO en Python"""
"""ENCAPSULAMIENTO"""

class A:
    def __init__(self):
        """Encapsulamiento débil"""
        self.inicial = 15
        self._contador = 0          #Definiendo mi atributo privado

    def incrementa(self):
        self._contador += 1

    def cuenta(self):
        return self._contador

class B:
    def __init__(self):
        """Encapsulamiento fuerte"""
        self.incial = True
        self.__contador = 0

    def incrementa(self):
        self.__contador += 1

    def cuenta(self):
        return self.contador

var_1 = A()
var_1._contador
var_1.inicial = 20

var_1.incrementa()
var_1.incrementa()
var_1.incrementa()
var_1.incrementa()

print(f"Valor inicial de A: {var_1.inicial}")
print(f"Contador A: {var_1._contador}")

var_2 = B()
var_2.inicial = False

var_2.incrementa()
var_2.incrementa()
var_2.incrementa()
var_2.incrementa()

print(f"Valor del contador de B: {var_2.inicial}")