def chequear_3_cifras(numero):
    return numero in range(100,1000)

resultado = chequear_3_cifras(568)
print(resultado)

##################################

def check_3_cifras(lista):
    for n in lista:
        if n in range(100,1000):
            return True

    return False

result = check_3_cifras([55,68,109])
print(result)

##################################
def check_return_3(lista):
    cifras_3 = []

    for n in lista:
        if n in range(100,1000):
            cifras_3.append(n)

    return cifras_3

result = check_return_3([55,68,109])
print(result)