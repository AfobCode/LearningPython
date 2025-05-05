## El modulo date time: almacenar hora y fecha en variables,
# calculos de tiempo
# mostrar en diferentes formatos

import datetime

mi_hora = datetime.time(17, 24, 55) #Formato de 24h, el primer numero es la hora, minutos, seg, ..
print(mi_hora)
print(mi_hora.hour)
print(mi_hora.minute)
print(mi_hora.second)

mi_fecha = datetime.date(2023, 1, 31)
print(mi_fecha)
print(mi_fecha.ctime())

hoy = datetime.date.today()
print(hoy)

###############################
from datetime import datetime

mi_fecha = datetime(2025, 1, 31, 18,25,46)
print(mi_fecha)

# Si quiero cambiar algo de la fecha uso el metodo replace
print(mi_fecha.replace(hour=14))
print(mi_fecha)
###############################
#Calcular el tiempo transcurrido enre dos fechas

from datetime import date
nace = date(1997,1,31)
hoy = date.today()

dias_vividos = hoy - nace
print(dias_vividos)
###############################
#Calcular horas de un turno
#from datetime import datetime

inicio = datetime(2023,1,26,14)
fin = datetime(2023,1,27,0,30)
print(f"su tunno empieza el ({inicio.ctime()}) y finaliza el ({fin.ctime()})")
turno = fin - inicio
print(f"Duro en total: {turno} es decir {turno.seconds} segundos")


tiempo_presente = datetime.now()
print(tiempo_presente)
print(tiempo_presente.minute)
