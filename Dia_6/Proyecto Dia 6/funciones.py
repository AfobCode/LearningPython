from pathlib import Path
from os import  remove
from os import system
def saludo(nombre):

    #Variables
    ruta = Path(Path.cwd().parents[3], 'Recetas', 'Recetas')
    num_recetas = 0

    #Conteo de recetas
    for receta in Path(ruta).glob('**/*.txt'):
        num_recetas += 1

    #Mostar informacion
    print(f"Bienvenido al recetario {nombre}")
    print(f"\nLas recetas estan almacendas en\n{ruta}")
    print(f"\nTenemos {num_recetas} recetas para que disfrutes")

    return ruta

def limpiar_pantalla():
    input("Para regresar presione enter")
    system('cls')
def revisar_seleccion(seleccion):
    valido = {'1', '2' , '3' , '4' , '5' , '6'}

    while seleccion not in valido:
        seleccion = input('Opcion Invalida, intente de nuevo: ')

    return int(seleccion)

def solicitar_info(*args):
    if len(args) == 0:
        categoria = input("Ingrese la categoria a la que pertenece la receta: ")
        nombre_receta = input("Ingrese el nombre de la receta: ")
    elif len(args) == 1:
        categoria = input("Ingrese la categoria a la que pertenece la receta: ")
        return categoria , False
    elif args[0] == 'N/A':
        categoria = input("Ingrese la categoria a la que pertenece la receta: ")
        nombre_receta = args[1]
    elif args[1] == 'N/A':
        categoria = args[0]
        nombre_receta = input("Ingrese el nombre de la receta: ")

    return categoria, nombre_receta

def mostrar_receta(ruta_base , categoria , receta):

    ruta = Path(ruta_base,categoria,receta)

    while not ruta.exists():
        if not ruta.parent.exists():
            print("Categoria incorrecta".center(60,"*"))
            categoria_act , receta_act = solicitar_info('N/A' , receta)

        else:
            print("Receta incorrecta".center(60, "*"))
            categoria_act , receta_act = solicitar_info(ruta.parent.name , 'N/A')

        ruta = Path(ruta_base , categoria_act , receta_act)

    return ruta.read_text()

def crear_receta(ruta_base , categoria):
    ruta = Path(ruta_base , categoria)

    if ruta.exists():
        nombre_receta = input('Ingrese el nombre de la receta: ')
        cuerpo_receta = input('Ingrese la receta: ')

        if Path(ruta, nombre_receta).exists():
            respuesta = f"Sobrescribio la receta '{nombre_receta}' exitosamente."
        else:
            respuesta = f"Receta '{nombre_receta}' creada exitosamente."

        Path(ruta ,nombre_receta).write_text(cuerpo_receta)
    else:
        respuesta = "No se puede crear receta. Categoria no registrada"

    return respuesta

def crear_categoria( ruta_base , categoria):
    try:
        Path(ruta_base, categoria).mkdir()
        resultado = f"La categoria {categoria} fue creada exitosamente"
    except:
        resultado = "La categoria que quiere crear ya existe"

    return resultado

def eliminar_receta(ruta_base, categoria , receta):

    ruta = Path(ruta_base, categoria , receta)

    if ruta.exists():
        remove(ruta)
        respuesta = f"La receta '{receta}' ha sido eliminada exitosamente"
    elif not ruta.parent.exists():
        respuesta = f"La categoria {categoria} no existe, no fue posible borrar la receta."
    else:
        respuesta = f"La receta '{receta}' no está en esta categoria, no fue posible borrar la receta."

    return respuesta

def eliminar_categoria(ruta_base , categoria):

    ruta = Path(ruta_base,categoria)

    if ruta.exists():
        for receta in ruta.glob('**/*.*'):
            eliminar_receta(ruta_base , categoria , receta.name)

        ruta.rmdir()
        respuesta = f"La categoria '{categoria}' y sus recetas fue eliminada exitosamente"
    else:
        respuesta = f"La categoria '{categoria}' no existe, no pudo ser eliminada"

    return respuesta
