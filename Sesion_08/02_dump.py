import json

"""Uso de la libería JSON"""

data_python = {"nombre": "Milagros", "edad": 20, "dstrito": "Jesús María", "promedio": 16.5}

"""Convirtiendo a un dato tipo Json: dumps()"""

data_python_to_json = json.dumps(data_python)

print(f"Nuestra variable contiene el siguiente dato: {data_python_to_json}")
print(type(data_python_to_json))