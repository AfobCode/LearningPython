from random import randint

aleatorio = randint(1,50)
print(aleatorio)
##############################
import random

aleatorio = round(random.uniform(1,10),2)
print(aleatorio)

aleatorio = round(random.random(),4) #numero aleatorio entre 0 y 1
print(aleatorio)

#Choice
#Selecciona un item aleatorio de una lista o de un objeto iterable
color = ['amarillo', 'azul', 'rojo', 'verde', 'negro']
aleatorio = random.choice(color)
print(aleatorio)

letras = "abdefghi"
aleatorio = random.choice(letras)
print(aleatorio)

#shuffle

numeros = list(range(100,1500, 100))
random.shuffle(numeros)
print(numeros)