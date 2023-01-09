nombre = "Carina"
print(nombre)

#nombre[0] = "K"
# Los str son inmutables, es decir no se pueden cambiar

n1 = "Kari"
n2 = "na"
print(n1 + n2)
print(n2*3) # Concatenara 3 veces el str almancenado en n2

poema = """Mil pequeños peces blancos
como si hirviera
el color del agua"""
print(poema)

print("agua" in poema)
print("sol" in poema)

print("sol" not in poema)

#La funcion len()
#Sirve para saber cuantos caracteres tiene una variable tipo str

print(len(poema))
print(len("Andres"))