lista = ['a', 'b', 'c', 'd']

for letra in lista:
    indice_letra = lista.index(letra) +1
    print(f"letra: {letra} esta en la posicion {indice_letra}")

###################################
lista = ["Pedro", "Paco", "Luis"]

for nombre in lista:
    if nombre.lower().startswith("p"):
        print(nombre)

###################################
numeros = [1,2,3,4,5]
mi_valor = 0

for numero in numeros:
    mi_valor = mi_valor + numero

print(mi_valor)

###################################
palabra = "Python"

for letra in palabra:
    print(letra)

print("\n")

for letra in "palabra":
    print(letra)

###################################
#Listas anidadas

for objeto in [[1,2],[3,4],[5,6]]:
    print(objeto)

for a , b in [[1,2],[3,4],[5,6]]:
    print(a,b)

###################################
#For loop en un diccionario

dic = {
    'clave1' : 'a',
    'clave2' : 'b',
    'clave3' : 'c'
}

for item in dic:
    print(item)

for clave ,valor in dic.items():
    print(clave,valor)