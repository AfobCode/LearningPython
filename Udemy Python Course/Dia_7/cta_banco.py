from os import system as sys

class Persona:

    #Metodo constructor
    def __init__(self, nombre , apellido):
        self.nombre = nombre
        self.apellido = apellido

class Cliente(Persona):

    def __init__(self, nombre , apellido,NroCuenta, balance):
        super().__init__(nombre, apellido)
        self.NroCuenta = NroCuenta
        self.balance = abs(balance)

    def __str__(self):
        info = " Informacion Usuario ".center(60,"*") +  f"\nNombre: {self.nombre}\nApellido: {self.apellido}\nNro de Cuenta: {self.NroCuenta}\nBalance: {self.balance:.2f}"

        return info

    def depositar(self , deposito):

        deposito = abs(deposito)
        self.balance += deposito

        return f"Se han depositado {deposito} pesos, su balance actual es de {self.balance:.2f} pesos."

    def retirar(self , retiro):

        retiro = abs(retiro)

        if retiro > self.balance:
            respuesta = f"Saldo insuficiente"
        else:
            self.balance -= retiro
            respuesta = f"Retiro exitoso\nRetiro por: {retiro}\nBalance Actual: {self.balance:.2f}"

        return respuesta


def crearCliente():
    nombre = input("Ingrese su nombre por favor: ")
    apellido = input("Ingrese su apellido por favor: ")
    nroCuenta = int(input("El numero de cuenta sera: "))
    blc = int(input("Ingrese el saldo para aperturar su cuenta: "))

    return Cliente(nombre, apellido , nroCuenta ,blc)

def limpiar_pantalla():
    input("Presione Enter para continuar")
    sys('cls')

def verificar_seleccion(seleccion):

    ops = list(range(1,5))

    try:
        seleccion = int(seleccion)
    except:
        seleccion = 0

    while seleccion not in ops:
        print('Opcion invalida')
        limpiar_pantalla()
        opcion = menu_opciones()
        seleccion = verificar_seleccion(opcion)

    return seleccion

def menu_opciones():

    seleccionar = input("""Ingrese la operacion que desea realizar: 
    [1] -> Consultar
    [2] -> Retirar
    [3] -> Depositar
    [4] -> Salir
    """)

    return seleccionar


def inicio():
    cliente = crearCliente()

    limpiar_pantalla()

    accion = menu_opciones()
    opcion = verificar_seleccion(accion)

    while opcion != 4:

        limpiar_pantalla()

        if opcion == 1:
            print(cliente)
        elif opcion == 2:
            valor = int(input("Ingrese el monto a retirar: "))
            retiro = cliente.retirar(valor)
            print(retiro)
        elif opcion == 3:
            valor = int(input("Ingrese el monto a depositar: "))
            deposito = cliente.depositar(valor)
            print(deposito)
        elif opcion == 4:
            print("Gracias por visitarnos feliz dia")
            break

        limpiar_pantalla()

        accion = menu_opciones()
        opcion = verificar_seleccion(accion)

inicio()