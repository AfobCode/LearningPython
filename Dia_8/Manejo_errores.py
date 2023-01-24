### La estructura es:
try:
    # Codigo que quiero probar
    pass
except:
    # Codigo a ejecurtar si ocurre un error en el try
    pass
else:
    # Codigo a ejecutar si no hay error en el try
    pass
finally:
    # Codigo que pase lo que pase se va a ejecutar
    pass

def suma():
    n1 = int(input("Ingrese el primer numero: "))
    n2 = int(input("Ingrese el segundo numero: "))
    print(n1 + n2)
    print("Gracias por sumar")
def majerar_errores_general():
    try:
        suma()
    except:
        print("Error!!\nNo se pudo sumar")
    else:
        print("Hiciste todo bien")
    finally:
        print("FIN")


def manejar_errores_concretos():
    try:
        suma()
    except TypeError: #Le digo que clase de error derivaria en esta respuesta
        print("Error!!\nEstas concatenando numeros con strings")
    except ValueError:
        print("Error!!\nNo es un número")
    else:
        print("Hiciste todo bien")
    finally:
        print("FIN")

manejar_errores_concretos()

########################################
#### Ejemplo ####

def pedir_numero():

    while True:
        try:
            numero = int(input("Ingrese el numero: "))
        except:
            print("Ese no es un numero")
        else:
            print(f"El numero ingresado es: {numero}")
            break

    print("Gracias Gonorriento")

pedir_numero()