
"""Conversión de datos"""

"""De string a tipo de dato int (entero)"""

var1 = "8000"
var2 = 35000
var3 = 400.0

suma1 = var2 + var3
print("El valor de sum1 es: {}".format(suma1))

# Esta suma no es posible por ser un valor string y otro por ser un valor entero
"""sum2 = var1 + var2
print("El valor de sum2 es: {}".format(suma2))"""

sum3 = int(var1) + var2
print("El valor de sum3 es: {}".format(sum3))

"""Suma de dos variables: int + float = """

sum4 = var2 + var3
print("El valor de sum4 es: {}".format(sum4))

var4 = int(sum4)
print(var4)

#Creamos nuevas variables
var5 = "700"
var6 = 40000
var7 = 40.68

"""La suma de las 3 variables como string"""
sum5 = var5 + str(var6) + str(var7)
print("El valor de sum5 es: {}".format(sum5))
