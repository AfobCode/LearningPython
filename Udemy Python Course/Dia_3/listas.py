mi_lista = ['a','b','c']
print(type(mi_lista))

otra_lista = ["hola", 5 , 7.8, True, ['a',4,7.9, False]]
print(type(otra_lista))

resultado = len(otra_lista)
print(resultado)

resultado = otra_lista[3]
print(resultado)

resultado = otra_lista[2:]
print(resultado)

mi_lista2 = ['d','e','f']
print(mi_lista + mi_lista2)

mi_lista3 = mi_lista + mi_lista2

mi_lista3[-1] = 'alfa' #Las listas son mutables, por tanto, puedo editar su contenido
print(mi_lista3)

#Si quiero agregar un elemento en la ultima posicion uso append
mi_lista3.append('g')
print(mi_lista3)

#SI quiero eliminar elementos de una lista uso pop()
mi_lista3.pop() #Elimina el ultimo elemento
mi_lista2.pop(2) #Elimina el elemento en el indice indicado
eliminado = mi_lista3.pop(2) #Tambien retorna el valor que fue eliminado

lista = [4,2,10,3,1]
print(lista)
lista.sort() #Este metodo no devuelve nada
print(lista)

lista = [4,2,10,3,1]
print(lista)
lista.reverse()
print(lista)

