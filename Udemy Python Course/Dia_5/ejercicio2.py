"""Escribe una función (puedes ponerle cualquier nombre que
quieras) que reciba cualquier palabra como parámetro, y que
devuelva todas sus letras únicas (sin repetir) pero en orden
alfabético."""

def letras_palabra(palabra):
    letrasUnicas = set(palabra)
    lista_letras = list(letrasUnicas)
    lista_letras.sort()

    return lista_letras

print(letras_palabra("entretenido"))