from timeit import timeit
from math import ceil

statement = """
from pathlib import Path
ruta = Path(Path.cwd(), 'Mi_Gran_Directorio')
coincidir(ruta)
"""

setup = """
from pathlib import Path
import os
import re
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
"""

duracion = timeit(statement, setup, number=100)
duracion = ceil(duracion)