"""Listas en Python"""

"""Listas (copy): Obtenemos todos los valores de una lista en otra variable"""

var_1 = ["SQLServer", "RDS", "mySQL", "postgreSQL"]

var_2 = var_1.copy()

print(var_1)

var_2.append("Oracle")
print("Los valores de mi variable var_2 es: {}".format(var_2))