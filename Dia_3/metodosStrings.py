txt = "Este es el texto de Federico"

resultado = txt
print(resultado)

#Metodo upper()
#convertir todo el string a mayusculas
resultado = txt.upper();
print(resultado)

resultado = txt[11:16].upper()
print(resultado)

#Metodo lower()
#convierte todo el string a minusculas
resultado = txt.lower()
print(resultado)

#Metodo Split()
#Toma un string dado y segun un caracter lo separa y devuelve una lista
resultado = txt.split() #Separa por espacios
print(resultado)

#Metodo join()
#Sirve para unir los datos almancenados en una lista
a = "Aprender"
b = "Python"
c = "es"
d = "Genial"
e = [a,b,c,d]
f = " ".join(e)
print(f)

#Metodo find()
#Es casi igual a index(), pero cuando no encuentra el sub_string en la cadena retorna -1 no un error
resultado = txt.find("z")
print(resultado)

#Metodo replace()
resultado = txt.replace("Federico","Andres")
print(resultado)