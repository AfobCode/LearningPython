from random import shuffle

#lista Inicial
palitos = ['-','--', '---', '----']

#mezclar palitos
def mezclar_palitos(lista_palitos):
    shuffle(lista_palitos)
    return lista_palitos

#pedirle intento
def probar_suerte():
    intento = 0

    while intento not in range(1,5):
        intento = int(input("Elige un numero del 1 al 4: "))

    return intento


#Comprobbar intento
def check_intento(lista,intento):
    if lista[intento -1] == '-':
        return "Perdio por loca"
    else:
        return "Se salvo perro"


resultado = check_intento(mezclar_palitos(palitos) , probar_suerte())
print(resultado)