texto = "ABCDEFGHIJKLM"
fragmento = texto[2]
print(fragmento)

fragmento = texto[2:5] #para extraer los caracteres contenidos entre el indice 2 hasta el indice 5-1
print(fragmento)

fragmento = texto[2:] #Extraer elementos desde el indice 2 hasta el final
print(fragmento)

fragmento = texto[:2] #Extraer los elementos desde el inicio hasta el indice 2-1
print(fragmento)

fragmento = texto[:10:2] #Extrae los elementos desde el primero hasta el 10-1 dando un paso de 2
print(fragmento)

fragmento = texto[::-1] #Extrae los elementos desde el inicio hasta el final, de manera inversa
print(fragmento)
