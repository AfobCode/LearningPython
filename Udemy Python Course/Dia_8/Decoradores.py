#Quiero que cada vez que ejecute alguna de las funciones de arriba imprima un
# saludo de hola, la funncion y adios

def decorar_saludo(funcion):
    def modificar_palabra(palabra):
        print('hola')
        funcion(palabra)
        print('adios')

    return modificar_palabra


def mayuscula(texto):
    print(texto.upper())


def minuscula(texto):
    print(texto.lower())

saludo_a_decorar = decorar_saludo(minuscula)

saludo_a_decorar('DENTRO DE OTRA FUNCION')