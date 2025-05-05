"""Escribe una función que requiera una cantidad indefinida de
argumentos. Lo que hará esta función es devolver True si en
algún momento se ha ingresado al numero cero repetido dos
veces consecutivas."""

def dos_ceros(*args):
    args = list(args)

    while 0 in args:
        index = args.index(0)
        if index + 1 == len(args):
            return False
        elif (args[index] == 0) and (args[index + 1] == 0):
            return True
        else:
            args.pop(index)

    return False

print(dos_ceros(5,6,1,0,0,9,3,5))
print(dos_ceros(0,0,9,3,5))
print(dos_ceros(5,6,1,0,0,9))
print(dos_ceros(5,6,1,0,0))
print(dos_ceros(5,6,1,0))
print(dos_ceros(6,0,5,1,0,3,0,1))