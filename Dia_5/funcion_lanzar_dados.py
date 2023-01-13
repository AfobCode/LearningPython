from random import randint

def lanzar_dados():
    return [randint(1, 6) for i in range(2)]

def evaluar_jugada(d1, d2):
    suma_dados = d1 + d2
    if suma_dados <= 6:
        return f"La suma de tus dados es {suma_dados}. Lamentable"
    elif (suma_dados > 6) and (suma_dados < 10):
        return f"La suma de tus dados es {suma_dados}. Tienes buenas chances"
    else:
        return f"La suma de tus dados es {suma_dados}. Parece una jugada ganadora"