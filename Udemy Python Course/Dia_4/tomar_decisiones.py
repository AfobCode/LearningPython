if 10 > 9:
    print("Es verdad, 10 mayor a 9")

if True:
    print("es correcto")
################################
x = True
if x:
    print("True")

################################
if 5 == 2:
    print("Correcto")
else:
    print("No es correcto")

################################

mascota = "perro"

if mascota == "Gato":
    print("Felicidades es un gato")
elif mascota == "perro":
    print("QUe chimba tener un perro")
else:
    print("No se que mascota tienes.")

################################
edad = 16
calificacion = 7.03

if edad < 18:
    print("Menor de edad")
    if calificacion >= 7:
        print("Aprobado")
    else:
        print("Reprobado")
else:
    print("Adulto")