
""""Diccionarios en Python"""

var_1 = {"nombre": "MySQL", "tipo": "BD relacional"}

"Convertiendo diccionarios a lista"
var_2 = list(var_1)

print("Mi diccionario convertido a lista es el siguiente: {}".format(var_2))

var_1_values = list(var_1.values())
print(var_1_values)

var_1_keys = list(var_1.keys())
print(var_1_keys)

var_3 = list(var_1.items())
print(var_3)