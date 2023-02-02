import os
import re
from pathlib import Path
import datetime
from desempenio import duracion


def coincidir(ruta):
    coincidencias = []
    for base , carpetas, archivos in os.walk(ruta):
        for archivo in archivos:
            ruta = Path(base,archivo)
            arch_texto = ruta.read_text()
            patron = r'N\w{3}-\d{5}'
            coincidencia = re.findall(patron,arch_texto)
            if len(coincidencia) > 0:
                coincidencias.append((archivo, coincidencia[0]))

    return coincidencias

def dia_busqueda():
    today = datetime.date.today().strftime("%d/%m/%y")
    return f"Fecha de busqueda: {today}"

def mostrar_resultados(resultados):
    texto = "ARCHIVO".ljust(20," ") + "\t" + "NRO. SERIE"
    texto += "\n"+"-"*15 + " "*5 + '\t' + "-"*15

    for arch , serie in resultados:
        texto += "\n"+arch.ljust(20," ") + "\t" + serie

    return texto

def separador():
    print("".center(70,"-"))

