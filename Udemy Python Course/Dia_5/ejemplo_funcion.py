#desempacar tuples

preciosCafe = [('capuchino',1.5),('Expresso',1.2),('Moka',1.9),('Moka',0.9),('Moka',1.7),('Moka',1.2),('Moka',3)]

for cafe,precio in preciosCafe:
    print(cafe)

#Quiero saber cual es el cafe mas caro

def cafe_caro(listaPrecios):
    cafeCaro = listaPrecios[0]
    for cafe in listaPrecios:
        if cafeCaro[1] < cafe[1]:
            cafeCaro = cafe

    return cafeCaro

resultado = cafe_caro(preciosCafe)
print(resultado)