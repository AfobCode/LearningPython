#Set
#Solo admiten elementos unicos
#No estan ordenados en indices
#Son inmutables
#No pueden tener ni listas ni diccionario

mi_set = set([1,2,3,4,5]) #Los sets solo aceptan un argumento, por tanto hay que pasarle un arreglo
print(mi_set, type(mi_set))

mi_set = {6,7,8,9}
print(type(mi_set), mi_set)

mi_set = set([1,1,1,1,2,2,2,4,5,6,7,2,2,2,24,5])
print(mi_set) #Solo alamacena elementos unicos

#No puedo almacenar listas o diccionarios en los sets porque son mutables
#De tal manera si pueden haber tuplas en los sets

mi_set = {1,2,3,(1,2,3)}
print(mi_set)
print(len(mi_set))
print(2 in mi_set)

s1 = {1,2,3}
s2 ={3,4,5}

s3 = s1.union(s2)
print(s3)

################################
#Metodo Add
s1.add(4)
print(s1)

#Metodo Remove
s1 = {'a','b','t'}
s1.remove('a')
print(s1)

#Metodo discard
s1.discard('x') #Elimina el elemento del set si lo tiene y sino lo ignora

#Metodo pop()
s1.pop() #Como los sets no tienen indices, elimina un elemento cualquiera

#Metodo clean()
s1.clear() #Vaciar el set