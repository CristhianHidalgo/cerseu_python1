"""Uso de librería de fecha y tiempo"""

from datetime import datetime, date

"""Obtener la fecha actual"""

fecha = date.today()
print(f"La fecha a manejar es la siguiente: {fecha}")

tiempo = datetime.now()
print(f"La fecha y hora a manejar es la siguiente: {tiempo}")

año = tiempo.year
mes = tiempo.month
dia = tiempo.day

print(f"El año acutal es: {año}")
print(f"El mes acutal es: {mes}")
print(f"El dia actual es: {dia}")

"""Uso del datetime para extrar la hora, el minuto y el segundo"""

hora = tiempo.hour
minuto = tiempo.minute
segundo = tiempo.second

print(f"La hora exacta son las {hora} con {minuto} minutos y {segundo} segundos")