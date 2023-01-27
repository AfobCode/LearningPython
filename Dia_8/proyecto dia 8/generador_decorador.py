"""
Para el proyecto dia 8 " Generador de turnos", este modulo va a contener
las funciones que decoran el turno y el generador de turnos
"""
from os import system

def generar_turno(area):
    """
    Esta funcion genera el turno deperndiendo del area que se pase como parametro
    :param area: area => tipo string, solo puede tener 3 valores, F, C, ó, P
    :return: genera un turno en tipo string
    """
    f , c , p = 0 , 0, 0

    while True:

        if area == 'F':
            f += 1
            turno = f"F - {f}"
        elif area == 'C':
            c += 1
            turno = f"C - {c}"
        else:
            p += 1
            turno = f"P - {p}"

        yield turno


def info_turno():
    """
    Esta funcion va a envolver el numero de turno con informacion contextual
    :param turno_funcion: funcion que va a generar el turno
    :return: un string de tres lineas, la forma de mostrar el turno al cliente
    """
    def entregar_turno(turno_generado):
        print("Su turno es: ")
        print(next(turno_generado))
        print("Aguarde su turno\npara ser atendido")

    return entregar_turno


def limpiar_pantalla():
    """Borrar la info de la consola, antes de continuar"""
    input("\nPresione la tecla enter para continuar ...")
    system('cls')


def verificar_seleccion(opcion):

    try:
        respuesta = int(opcion)
    except:
        respuesta = 0

    while respuesta not in range(1,5):
        print("Seleccione 1 , 2, 3 o 4")
        seleccion = solicitar_info()
        respuesta = verificar_seleccion(seleccion)

    return respuesta


def solicitar_info():
    return input("""
    Seleccione el area a la que se dirige: 
        [1] -> Farmacia
        [2] -> Perfumes
        [3] -> Cosmeticos
        [4] -> Salir
    """)


turno_farmacia = generar_turno('F')
turno_cosmetico = generar_turno('C')
turno_perfume = generar_turno('P')

entregar_turno = info_turno()
