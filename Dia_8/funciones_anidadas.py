def mayusculas(texto):
    print(texto.upper())

def minusculas(texto):
    print(texto.lower())

#Quiero que cada vez que ejecute alguna de las funciones de arriba imprima un
# saludo de hola, la funncion y adios

#Un forma seria: (nada eficiente)
print("Buenas")
mayusculas("que se dice")
print("vemos")

#Otra forma es agrar los print detro de la funcion
def mayuscula_saludo(texto):
    print("Buenas")
    print(texto.upper())
    print("vemos")

#############################
#Es aca donde toman valor los operadores
# Todas las funciones son objetos
# Por lo tanto puede pasarse a otra funcion como argumento
# similar a los callbacks en JS

def cambiar_letras(tipo):

    def mayuscula(texto):
        print(texto.upper())

    def minuscula(texto):
        print(texto.lower())

    if tipo == "may":
        return mayuscula
    elif tipo == "min":
        return minuscula

operacion = cambiar_letras('may')
operacion('palabra')