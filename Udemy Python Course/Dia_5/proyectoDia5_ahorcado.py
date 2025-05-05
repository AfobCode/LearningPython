from proyectoDia5_ahorcado_wordlist import word_list
from random import choice
###################################
#Definicion de funciones.py
def revisar_letra(letra, palabra:str):
    palabra = palabra.lower()
    indices = []

    if letra not in palabra:
        return False
    else:
        plb = list(palabra)
        for indice , value in enumerate(plb):
            if value == letra:
                indices.append(indice)

    return indices
def sustituir(letra, guiones,inidices):
    g = list(guiones)
    for indice in inidices:
        g[indice] = letra

    palabra_act = "".join(g)

    return palabra_act
def revisar_palabra(palabra):
    if "_" not in palabra:
        return True
    else:
        return False
def intentos(palabra):
    letras_unicas = set(palabra)
    n_intentos = len(letras_unicas) + 3
    return n_intentos

###################################
#Definicion de Variables
palabra = choice(word_list)
palabra_oculta = "_"*len(palabra)
print(palabra)
intento = intentos(palabra)
letras_erradas = ""

###################################
#Inicio
print(" Ahorcado ".center(60,'-'))
print(f"Tiene {intento} intentos para adivinar")

###################################
#Flujo del programa
for i in range(intento):
    l = input("Ingresa una letra: ").lower()
    r_l = revisar_letra(l,palabra)

    if r_l == False:
        letras_erradas += f"{l}/"
        print(f"Estas letras no estan en la palabra: {letras_erradas}")
        print(palabra_oculta,"\n")
        continue
    else:
        palabra_oculta = sustituir(l,palabra_oculta,r_l)
        print(palabra_oculta, "\n")

    if revisar_palabra(palabra_oculta):
        print(f"Felicitaciones!! adivinaste la palabra: {palabra}")
        break
else:
    print("Fin del juego, gracias por participar")

