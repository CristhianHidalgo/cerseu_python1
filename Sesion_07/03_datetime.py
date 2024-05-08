"""Uso de librería de fecha y tiempo"""

"""
    Conversión de fechas
"""

import datetime

fecha_1 = datetime.datetime(2023, 4, 13)  # Tipo de dato datime
fecha_2 = datetime.datetime(2023, 4, 19)  # Tipo de dato datime

if fecha_1 == fecha_2:
    print("Nacieron el mismo día")
elif fecha_1 > fecha_2:
    print("El niño 2 es mayor que el nuño 1")
else:
    print("El niño 1 es mayor que el nuño 2")