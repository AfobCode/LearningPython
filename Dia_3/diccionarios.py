#Los diccionarios
#No tienen ningun orden, por tanto no tienen indices
#Se alamacenan los datos de manera llave:valor
#por tanto, las claves no se pueden repetir en un diccionario

diccionario = {
    "c1": "Valor1",
    "c2": "Valor2",
    "c3": "Valor3"
}

print(diccionario, type(diccionario))
resultado = diccionario["c2"]
print(resultado)


cliente = {
    "nombre":"Juan",
    "Apellido":"Fuentes",
    "peso": 88.5,
    "Talla": 32
}

consulta = cliente["peso"]
print(consulta)

########################################

dic = {
    'c1': 55,
    'c2': [10,20,30],
    'c3':{
        's1':100,
        's2':200
    }
}

print(dic['c2'][0])
print(dic['c3']['s1'])

########################################
#Hacer que la letra 'e' se imprima en mayuscula

dic = {
    'c1':['a','b','c'],
    'c2':['d','e','f']
}

print(dic['c2'][1].upper())
########################################
#Agregar elemntos a un diccionario

dic = {1:"a",2:"b"}
dic[3] = "c" #Uso el [] para indicarle el nombre de la llave
print(dic)

#Sobreescribir/Actualizar un llave
dic[2] = "z"

#Saber todas la claves de un dict
print(dic.keys())

#Saber todos los valores
print(dic.values())

#Saber todas las llaves y los valores
print(dic.items())