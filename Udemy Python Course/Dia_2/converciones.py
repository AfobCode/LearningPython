#Conversiones implicitas
#Aquellas conversines que Python hace automaticamente
#Sin que yo lo declare

num1 = 10
print( num1, type(num1))
num2 = 23.6
num1 = num1 + num2 # Aca python implicitamente convierte a num1 de int a float

print(num1, type(num1),num2,type(num2))

#Conversione explicitas
#Soy yo quien le pide a python que convierta el tipo de dato a otro

num3 = 4.5
print(num3, type(num3))
num3 = int(num3)
print(num3, type(num3))

#La funcion input() crea un string de forma predeterminada

edad = input("Dime tu edad: ")
print(edad, type(edad))
edad = int(edad)
print(edad, type(edad))
