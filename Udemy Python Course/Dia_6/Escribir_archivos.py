#Para abrir un archivo de texto, python y la funcion open
#ofrecen 3 opciones, 'r' de read, es el que usa por defecto
# 'w' que si no existe un archivo con ese nombre crea un archivo nuevo
# pero si ya existe ese archivo lo va a sobreescribir por completo
# borrando la informacion que el archivo contenia previamente
# 'a' de append, en este caso si el archivo no existe creara uno nuevo
# pero si el archivo existe, agregara el texo al final del archivo
# y no lo va a sobreescribir, solo agregar

#####################################
#Abrir un archivo de texto en modo lectura
archivo = open('Prueba.txt', 'r')
print(archivo.read())
archivo.close()

#####################################
#Crear un archivo nuevo o sobreescribir
archivo = open('prueba1.txt', 'w')
archivo.write('Este es un archivo nuevo\n')
archivo.write('''
Escribir varias lineas
sin tener que escapar 
el salto de linea.
''')
archivo.writelines(['Hola Mundo','con el metodo','writelines'])
#Si quiero usar una lista que añada lineas a un archivo podria usar
#un looo for de la siguiente manera

lista = ['Hola Mundo','Cada linea','fue agregada', 'en iteraciones de un loop', 'el loop for']

for linea in lista:
    archivo.write(linea + '\n')

archivo.close()

#####################################
#Crear un archivo nuevo o agregar informacion
archivo = open('Prueba.txt', 'a')
archivo.write('nueva linea agregada al final de un archivo de texto')
archivo.close()