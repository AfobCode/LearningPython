############################################
#Objeto counter

from collections import Counter

numeros = [8,6,9,5,4,5,5,5,8,7,4,5,4,4]
print(Counter(numeros))

ciudad = "Mississippi"
print(Counter(ciudad.lower()))

frase = "al pan , pan ; y al vino , vino"
print(Counter(frase.split(' ')))

serie = Counter([1,1,1,1,1,1,1,2,2,2,2,2,2,2,2,2,3,3,3,3,3,3,4,4,4,4,4])
print(serie.most_common()) #Me devuelve el valor que mas veces esta almanenado en el objeto count
print(serie.most_common(1))
print(serie.most_common(3))

############################################
#Objeto defaultdict

from collections import defaultdict

mi_dict = {'uno':'verde','dos':'azul' , 'tres': 'rojo'}
try:
    print(mi_dict['cero']) #Clave que no existe
except KeyError:
    print("Clave no almacenada en el diccionario")

nuevo_dict = defaultdict(lambda: 'Nada') #En caso que yo quiera imprimir una clave que no este en el diccionario me va a devolver nada
nuevo_dict['Uno'] = 'verde'
print(nuevo_dict['cero']) # me ahorra tener que pasar por un try. Y agrega esa llave:valor al diccionario
print(nuevo_dict.items())

############################################
#Objeto namedtuple

from collections import namedtuple
miTupla = (500, 18, 65)
print(miTupla[1])

Persona = namedtuple('Persona',['nombre','altura','peso']) #Creo un objeto de tipo namedtuple
ariel = Persona('Ariel',1.76,79) #Creo una instancia del objeto persona

print(ariel.altura)
print(ariel[1])
print(ariel,type(ariel))
