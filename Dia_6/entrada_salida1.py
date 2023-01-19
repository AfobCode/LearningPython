mi_archivo = open('Prueba.txt') # Abro el archivo

#print(mi_archivo) #Va a imprimir el objeto y la info del objeto
#print(mi_archivo.read())  #Lee la informacion en el objeto

unaLinea = mi_archivo.readline() #Imprime la primera linea
#Por mas veces que le pida a python que imprima una linea no va a iterar en el archivo
print(unaLinea)
print(unaLinea)
print(unaLinea)

#Pero si ejecuto el metodo readline varias veces, en ese caso
#si ira imprimiendo cada linea del archivo
unaLinea = mi_archivo.readline() #Segunda vez que llamo al metodo, por lo tanto la segunda linea sera impresa
print(unaLinea)

unaLinea = mi_archivo.readline() #Tercera vez que llamo al metodo, imprime la linea 3
print(unaLinea)

#La variable unaLinea es de tipo string, por tanto podre utilizar todos los metodos
#de los strings upper, lower, strip, split, etc.
unaLinea.str
print(unaLinea.upper())
print(unaLinea.lower())
print(unaLinea.split(' '))
mi_archivo.close() #Cierro el archivo

# Tambien puedo iterar por linea en el archivo de texto.

mi_archivo_loop = open('Prueba.txt')

print("For Loop".center(60,"*"))
for linea in mi_archivo_loop:
    print("Aca dice: " , linea)


mi_archivo_loop.close()

#Metodo readlines()

mi_archivo = open('Prueba.txt')

print("Metodo readlines()".center(60,"*"))
todas = mi_archivo.readlines() # Me devuelve una lista donde cada elemento es una linea
print(todas)

todas = todas.pop(0) #Puedo usar metodos para editar la variable todas, mas no voy a editar el archivo original
print(todas)

mi_archivo.close()









