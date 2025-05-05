from random import choice

def lanzar_moneda():
    return choice(["cara", "cruz"])

def probar_suerte(moneda,lista):
    if (moneda == 'Cara'):
        print("La lista se autodestruirá")
        lista.clear()
        return lista
    else:
        print("La lista fue salvada")
        return lista

