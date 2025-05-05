class Animal:

    def __init__(self, edad, color):
        self.edad = edad
        self.color = color
    def nacer(self):
        print("Este animal ha nacido")

class Pajaro(Animal):
    pass
class Perro(Animal):
    pass

print(Pajaro.__bases__) #Muestra la clase padre de una clase
print(Animal.__subclasses__()) #Muestras las clases hijo de una clase

piolin = Pajaro(2,'Amarillo')
print(piolin.color)
piolin.nacer()