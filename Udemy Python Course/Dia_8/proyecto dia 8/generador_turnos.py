"""
Crear un progroma que le pregunte al cliente a cual de las areas de la farmacio se dirige
para generar un turno.
"""


from generador_decorador import limpiar_pantalla , solicitar_info, verificar_seleccion
from generador_decorador import turno_farmacia, turno_cosmetico, turno_perfume, entregar_turno

def inicio():

    """
    Esta funcion imprimira en pantalla el turno asignado a cada cliente
    :return: None
    """
    opcion = solicitar_info()
    seleccion = verificar_seleccion(opcion)

    limpiar_pantalla()

    while seleccion != 4:
        if seleccion == 1:
            entregar_turno(turno_farmacia)
        elif seleccion == 2:
            entregar_turno(turno_perfume)
        else:
            entregar_turno(turno_cosmetico)

        limpiar_pantalla()

        opcion = solicitar_info()
        seleccion = verificar_seleccion(opcion)

        limpiar_pantalla()

    print("Gracias por visitarnos, feliz tarde")

inicio()
