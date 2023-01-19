#En la definicio de funciones.py cuando uso el *args
#Cuando se definen los argunmentos le estoy indicando a Python
#Que no hay una cantidad de argumentos definido
#y el usuario podra ingresar tantos argumentos como quiera

#usar *args es una buena practica sin embargo cada vez que
#en la definicion de la funcion la palabra o letra que nombra
#los argumentos este precedida por un * python interpretara
#que no hay una cantidad de variables predefinida.
def suma(*args):
    total = 0
    for arg in args:
        total += arg

    return total

def sumaNum(*nums):
    return sum(nums)

def tipoArgs(*args):
    return type(args) #los argumentos que pasan a *args, seran almacenados como tuplas en args

#las funciones.py suma y sumaNum son iguales

print(suma(10,20,15,25))
print(suma(10,20))
print(sumaNum(10,20,15,25))
print(sumaNum(10,20))
print(tipoArgs(10,20,15,25))