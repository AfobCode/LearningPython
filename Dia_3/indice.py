mi_texto = "Esta es una prueba"
resultado = mi_texto[0]
print(resultado)

resultado = mi_texto[9]
print(resultado)

resultado = mi_texto[-1] #ultimo caracter
print(resultado)

resultado = mi_texto.index("n")
print(resultado) #Indica el indice del sub_string

resultado = mi_texto.index("una") #Me inidica el indice de la primera letra del sub_string
print(resultado)

#La funcion index() una vez que encuentra el sub_string
#retorna el primer indice que encuentra

resultado = mi_texto.index("e") #va a retornar el valor del indice de la primera e minuscula que encuentre
print(resultado)

#En este caso yo le puedo indicar a la funcion la parte en la que
#Yo quiero que busque dicho sub_string

resultado = mi_texto.index("e",6) #Quiero que inicie buscando la e desde el indice 6 en adelante
print(resultado)

resultado = mi_texto.index("s",5,10) #Va a buscar el indice de la letra a entre el indice 5 y el indice 9
print(resultado)

#La funcion str.rindex() buscara en el string un sub_string dado
#pero lo buscara de derecha a izquierda (al reves)

resultado = mi_texto.rindex("e")
print(resultado)


