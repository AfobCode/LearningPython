# Quiero crear un funcion que me devuelva el numero 4

#Funcion normal
def numero_4():
    return 4

#Funcion generadora

def generar_4():
    yield 4

print(numero_4())
print(generar_4())

#Para producir el 4 debo usar la funcion next()
print(next(generar_4()))

###################################
############## Ejemplo ############

#Nececito un funcion que me devuelva una lista de numeros del 1 al 4
# pero multiplicado por 10
def lista_normal():
    return [x * 10 for x in range(1,5)]

def lista_generada():
    for x in range(1,5):
        yield x * 10

print(lista_normal()) # Aca ya me devuelve toda la lista [10 , 20, 30 ,40] ocupa mas espacio
print(next(lista_generada())) # Aca me devuelve solo el 10, produjo el primer numero de la lista
print(next(lista_generada())) # Aca genera el segundo numero, 20

###################################
############## Ejemplo ############

def generador():
    x = 1
    yield x # Primero llega aca y retorna x

    x += 9
    yield x # Cuando se llama de nuevo viene este punto y devuelve el valor actualizado

    x += 90
    yield # Cuando se llama de nuevo viene este punto y devuelve el valor actualizado

g = generador()

print(next(g))
print("Paso intermedio")
print(next(g))
print("Ejecuto el codigo que se encontraba despues del primer yield y salio con el segundo yield")
print(next(g))
print("Ejecuto el codigo entre el segundo y el utimo yield")























