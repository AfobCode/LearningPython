#Enlazar dos o mas listas enlazando sus elementos en tuples
#Devuelve una lista de tuples en donde cada elemento esta enlazado

nombres = ['Ana', 'Hugo', 'Valeria']
edades = [65, 29,42]

combinados = zip(nombres , edades)
print(combinados)

#Tengo que castear/parsear combinados en una lista
#para que el objeto se imprima

combinados = list(combinados)
print(combinados)

#Puede tener mas de dos listas
nom = ['Ana', 'Hugo', 'Valeria']
edad = [65, 29,42]
ciudades = ['Bogota', 'Buenos Aires', 'Santiago']

combinados = list(zip(nom,edad,ciudades))
print(combinados)

for nombre , edad , ciudad in combinados:
    print(f"{nombre} tiene {edad} años y vive en {ciudad}")