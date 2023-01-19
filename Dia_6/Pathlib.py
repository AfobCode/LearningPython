from pathlib import Path, PureWindowsPath

carpeta = Path('/Users/Andres Felipe/Documents/Mision_TIC_2022/python/Udemy_python/Python TOTAL - Programador Avanzado en 16 días/Dia_6/Prueba.txt')
carpeta2 = Path('/Users/Andres Felipe/Documents/Mision_TIC_2022/python/Udemy_python/Python TOTAL - Programador Avanzado en 16 días/Dia_6/Pueba.txt')

if not carpeta.exists():
    print('El archivo NO existe')
else:
    print(f'{carpeta.name} cargado')
    print(carpeta.read_text())
    print(carpeta.name)
    print(carpeta.suffix)
    print(carpeta.stem)

#PureWindowsPath

#Transformar un path en un path valido para Windows
wnd_pathh = PureWindowsPath(carpeta)
print(wnd_pathh)