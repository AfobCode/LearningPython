from funciones import *

#Iniciacion del recetario
usuario = input("Ingrese su nombre por favor: ")

while True:
    ruta = saludo(usuario)
    opcion = revisar_seleccion(input("Ingrese la accion que quiere realizar: "))

    if opcion ==1:

        categoria , receta = solicitar_info()
        resultado = mostrar_receta(ruta , categoria , receta)

    elif opcion == 2:
        categoria , receta = solicitar_info('Preguntar Categoria' )
        resultado = crear_receta(ruta , categoria)

    elif opcion == 3:
        categoria , receta = solicitar_info('Preguntar Categoria')
        resultado = crear_categoria(ruta , categoria)

    elif opcion == 4:
        categoria, receta = solicitar_info()
        resultado = eliminar_receta(ruta, categoria , receta)

    elif opcion == 5:
        categoria, receta = solicitar_info('Preguntar Categoria')
        resultado = eliminar_categoria(ruta, categoria)

    elif opcion == 6:
        print("Has seleccionado salir de recetario, Feliz Dia Perro")
        break

    print(resultado)
    limpiar_pantalla()