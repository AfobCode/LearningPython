"""Crea un generador (almacenado en la variable generador) que sea capaz de devolver una secuencia infinita de números, iniciando desde el 1,
y entregando un número consecutivo superior cada vez que sea llamada mediante next."""

def infinito():
    x = 0
    while x >= 0:
        x += 1
        yield x

generador = infinito()

print(next(generador))
print(next(generador))
print(next(generador))
print(next(generador))
print(next(generador))