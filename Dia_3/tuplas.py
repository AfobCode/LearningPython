#Tuplas
#Las tuplas son inmutables
#Ocupan menos espacio en memoria que las listas
#Para almancenar estructuras que no puedan ser editadas

mi_tupla = (1,2,3,4,5)
print(mi_tupla,type(mi_tupla))

mi_tupla = 1,2,3,4,5 #No es necesario usar los parentesis
print(mi_tupla,type(mi_tupla))

t = 5,5.6,True,['z','y'] #Cualquier tipo de dato puede ser almacenado en tuplas
print(t,type(t))
print(t[-1])

mi_tupla = ((10,20),(40,50))
print(mi_tupla[1][0])