"""Uso de librería de fecha y tiempo"""

from datetime import datetime

str_data = "12/6/2024"

"""
    d: día
    m: mes
    Y: año
"""
conversion = datetime.strptime(str_data, "%m/%d/%Y")
print(f"La fecha fomateada es: {conversion}")

"""Traer el mes de la fecha con formato de letras: strftime de dateime"""

conversion_mes = datetime.strftime(conversion, "%d %b del %Y")
print(f"Nuestra fecha con cambio del mes es el sigueinte: {conversion_mes}")