from os import system
from pathlib import Path
nombre = input("Dime tu nombre: ")
edad = input("Dime tu edad: ")

system('cls') #Va a limpriar la infomacion de la consola

print(f"Tu nombre es {nombre} y tienes {edad} años")

Path.parents