"""Crea una función llamada devolver_distintos() que reciba 3
integers como parámetros.
Si la suma de los 3 numeros es mayor a 15, va a devolver el
número mayor.
Si la suma de los 3 numeros es menor a 10, va a devolver el
número menor.
Si la suma de los 3 números es un valor entre 10 y 15
(incluidos) va a devolver el número de valorintermedio."""

def devolver_distintos(n1,n2,n3):
    print("Nuevo llamado".center(40,"-"))
    lista = [n1,n2,n3]
    if sum(lista) > 15:
        return max(lista) , sum(lista)
    elif sum(lista) <10:
        return min(lista) , sum(lista)
    else:
        print(sum(lista))
        lista.remove(max(lista))
        lista.remove(min(lista))
        return lista[0]

print(devolver_distintos(10,20,50))
print(devolver_distintos(1,2,3))
print(devolver_distintos(5,4,1))
print(devolver_distintos(10,4,1))
print(devolver_distintos(7,5,2))
