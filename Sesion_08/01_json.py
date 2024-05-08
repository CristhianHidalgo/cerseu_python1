"""Uso de lalbrería JSON para tratar tipos de datos JSON"""

import json

"""Uso de la librería JSON"""
json_data = '{"nombre": "Python", "tipo": "Backend", "paradigma": "POO"}'

json_to_python = json.loads(json_data)

print(f"Nuestro dato tipo JSON a dato para PYthon es: {json_to_python}")
print(type(json_to_python))