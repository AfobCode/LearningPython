import os
import shutil
import send2trash

#Saber en que directorio estoy
print(os.getcwd())

#Crear un achivo aca
archivo_vacio = open('curson.txt','w')
archivo_vacio.close()

#Listar los archivos de mi directorio actual
print(os.listdir())

#Mover un archivo de carpeta
#shutil.move('curson.txt', 'C:\\Users\\Andres Felipe\\Documents\\Mision_TIC_2022\\Python\\Udemy_python\\Python TOTAL - Programador Avanzado en 16 días')

#Para borrar un archivo
#shutil.rmtree() #Va a eliminar la carpeta de la de la ruta que se le pase y todos los archivos contenidos en ella definitivamente

#Utilizar una libreria fuera de python send2trash
## Si el modulo no esta instalado pip install send2trash
#send2trash.send2trash('C:\\Users\\Andres Felipe\\Documents\\Mision_TIC_2022\\Python\\Udemy_python\\Python TOTAL - Programador Avanzado en 16 días\\curson.py')

# Metodo walk => Es un generador
# Recorre todos los archivos, carpetas y subpetas de una ruta reterminada
ruta = os.walk('C:\\Users\\Andres Felipe\\Documents\\Mision_TIC_2022\\Python\\Udemy_python')

print(next(ruta))
