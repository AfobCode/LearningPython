#Booleano
#Solo puede tomar valores de True o False

var1 = True
var2 = False

print(type(var1),var1)

#Crear un Bool, de manera indirecta mediante una comparacion
numero = 1 < 3
print(type(numero), numero)

numero = 5 == 2+3 #Es igual?
print(type(numero), numero)

numero = 5 != 2+3 #Es diferente?
print(type(numero), numero)

numero = bool(5 != 2+3) #Es diferente?
print(type(numero), numero)

lista = [1,2,3,4,5]
control = 5 in lista
print(type(control), control)

control = 5 not in lista
print(type(control), control)