lista_numeros = [1,2,15,7,2]

def reducir_lista(lista):
    lista.remove(max(lista_numeros))
    return set(lista)

resultado = reducir_lista(lista_numeros)
print(len(resultado))
for i in resultado:
    print(i)