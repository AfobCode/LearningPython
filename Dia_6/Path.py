from pathlib import Path

guia = Path("Barcelona", "Sagrada_Familia")
#Crear una ruta relativa con los parametros que se le han pasado
print(guia)

#Para obtener una ruta absoluta del usuario actual
base = Path.home()
print(base , guia)

#La funcion path acepta strings y otros objetos de tipo path
guia = Path(base, 'europa', 'españa', Path('Barcelona' , 'Sagrada Familia.txt'))
#El primer argumento que se le paso fue un objeto Path.home()
#Los argumentos 2 y 3 son strings
#y el cuarto argumento fue un objeto tipo Path()
print(guia)

guia2 = guia.with_name("La_Pedrera.txt")
print(guia2)

print(guia.parent)
print(guia.parent.parent)

#############################################
guia = Path("Europa", "España" , "Barcelona" , "Sagrada_Familia.txt")
en_europa = guia.relative_to(Path("Europa"))
en_espania = guia.relative_to(Path("Europa","España"))

print(en_espania)
print(en_europa)

