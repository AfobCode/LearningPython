from pathlib import Path
from desempenio import duracion
from funciones import  separador ,dia_busqueda, coincidir , mostrar_resultados

def inicio():
    ruta = Path(Path.cwd().parent, 'Mi_Gran_Directorio')
    resultado = coincidir(ruta)

    separador()
    print(dia_busqueda())
    print("\n")
    print(mostrar_resultados(resultado))
    print("\n")
    print(f"Números encontrados: {len(resultado)}")
    print(f"Duracion de la busqueda: {duracion:.2f}")
    separador()

inicio()