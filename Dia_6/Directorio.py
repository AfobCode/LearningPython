import os #importar modulo os Operating System

ruta = os.getcwd() #metodo get Current Working Directory
print(ruta)

#metodo change directory, para cambiar el directorio de trabajo actual
os.chdir('C:\\Users\\Andres Felipe\\Documents\\Mision_TIC_2022\\Python\\Udemy_python\\')

#metodo para crear una carperta
nuevaCarpeta = os.makedirs('C:\\Users\\Andres Felipe\\Documents\\Mision_TIC_2022\\Python\\Udemy_python\\Python TOTAL - Programador Avanzado en 16 días\\Dia 6 Carpeta')

#Metodo para obtener la ruta o el nombre del archivo
ruta = 'C:\\Users\\Andres Felipe\\Documents\\Mision_TIC_2022\\Python\\Udemy_python\\Python TOTAL - Programador Avanzado en 16 días\\Dia_6\\Prueba.txt'
#La variable ruta, es una ruta completa, tiene el directorio y el nombre del archivo
print(os.path.basename(ruta)) #Imprimira en consola el nombre del archivo
print(os.path.dirname(ruta)) #Imprimira en consola el directorio, la ruta
print(os.path.split(ruta)) #Imprimira una tupla con el directorio en el primer argumento y el nombre del archivo como segundo argumento

#Metodo para borrar una carpeta de un directorio
os.rmdir('C:\\Users\\Andres Felipe\\Documents\\Mision_TIC_2022\\Python\\Udemy_python\\Python TOTAL - Programador Avanzado en 16 días\\Dia 6 Carpeta')

###################################################
from pathlib import Path

carpeta = Path('/Users/Andres Felipe/Documents/Mision_TIC_2022/Python/Udemy_python/Python TOTAL - Programador Avanzado en 16 días')
archivo = carpeta / 'otro_archivo.txt'