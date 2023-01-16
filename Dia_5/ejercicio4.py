"""Escribe una función llamada contar_primos() que requiera un
solo argumento numérico.
Esta función va a mostrar en pantalla todos los números
primos existentes en el rango que va desde cero hasta ese
número incluido, y va a devolver la cantidad de números
primos que encontró.
Aclaración, por convención el 0 y el 1 no se consideran primos."""

def contar_primos(n):
    primos = [2]
    for i in range(2,n+1):
        primo = True
        for p in primos:
            if i % p == 0:
                primo = False
                break

        if primo == True:
            primos.append(i)

    return primos , len(primos)

print(contar_primos(50))