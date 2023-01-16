#**kwards = 'key word args' => Trabaja con diccionarios
#una cantidad de elemetos indeterminados

def suma(**kwargs):
    return (type(kwargs))

print(suma(x = 3, y = 6, z = 7)) #como si estuviera creando un diccionario con un constructor

def sumaKeyVal(**kwargs):
    for clave, valor in kwargs.items():
        print(f"{clave} almacena el valor: {valor}")

    total = sum(kwargs.values())

    return total

print(sumaKeyVal(x = 3, y = 6, z = 7))

# Al definir una funcion primero debo ingresar los argumentos comunes
# luego los argumentos que van a ser *args y finalmente **kwargs

print(" Args y Kwars ".center(40, "#"))
def pruebaArgsKwargs(n1,n2, *args,**kwargs):
    print("\nVariables normales: ", n1, " y ",n2)

    print("\nValores almacenados en args: ")
    for arg in args:
        print(arg)
    print("\nValores almacenados en kwargs: ")
    for clave , valor in kwargs.items():
        print(clave, "contine" , valor)

    return type(n1), type(n2) , type(args) , type(kwargs)

n1Type , n2Type , argsType , kwargsType = pruebaArgsKwargs(True,"Andres", 100,40,50,500, x = "Uno" , y = True, z = 3)

print(n1Type , n2Type , argsType , kwargsType)