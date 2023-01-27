"""
Quiero saber cual de las dos funciones tarda menos tiempo en
ejecutarse, es decir, saber cual es mas eficiente
prueba_for vs prueba_while
"""
import datetime


def prueba_for(n):
    lista = []
    for i in range(1,n+1):
        lista.append(i)

    return lista

def prueba_while(n):

    lista = []
    contador = 1
    while contador <= n:
        lista.append(contador)
        contador +=1

    return lista

def prueba_for_mejorado(n):
    lista = [i for i in range(1,n+1)]
    return lista

import time

inicio = time.time()
prueba_for(1000000)
fin = time.time()
pf = fin - inicio

inicio = time.time()
prueba_while(1000000)
fin = time.time()
pw = fin - inicio

inicio = time.time()
prueba_for_mejorado(1000000)
fin = time.time()
pfm = fin - inicio

tiempos = [pf,pw,pfm]
print(tiempos)

#Para iteraciones mas pequeñas, tipo 100 o 10
#el modulo time no va a detectar esas pequeñas diferencias

inicio = time.time()
prueba_for_mejorado(100)
fin = time.time()
print(fin-inicio)

# En estos casos es mejor usar el modulo timeit

import timeit
statement_timeit_pf = """
prueba_for(10)
"""

setup_timeit_pf = """
def prueba_for(n):
    lista = []
    for i in range(1,n+1):
        lista.append(i)

    return lista
"""
pf_duracion = timeit.timeit(statement_timeit_pf,setup_timeit_pf, number= 10000) # el number hace referencia all numero de veces que va a repertir el codigo para validar el tiempo que tarda

statement_timeit_pw = """
prueba_while(10)
"""

setup_timeit_pw = """
def prueba_while(n):

    lista = []
    contador = 1
    while contador <= n:
        lista.append(contador)
        contador +=1

    return lista
"""
pw_duracion = timeit.timeit(statement_timeit_pw,setup_timeit_pw, number= 10000) # el number hace referencia all numero de veces que va a repertir el codigo para validar el tiempo que tarda

statement_timeit_pfm = """
prueba_for_mejorado(10)
"""

setup_timeit_pfm = """
def prueba_for_mejorado(n):
    lista = [i for i in range(1,n+1)]
    return lista
"""
pfm_duracion = timeit.timeit(statement_timeit_pfm,setup_timeit_pfm, number= 10000) # el number hace referencia all numero de veces que va a repertir el codigo para validar el tiempo que tarda

duracion = [pf_duracion,pw_duracion,pfm_duracion]
print(duracion)

