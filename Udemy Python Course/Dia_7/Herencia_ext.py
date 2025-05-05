class Animal:
    def __init__(self, edad , color):
        self.edad = edad
        self.color = color

    def nacer(self):
        print("Este animal ha nacido")

    def hablar(self):
        print("Este animal emite un sonido")

class Pajaro(Animal):

    def __int__(self, edad , color, altura_maxima):
        super().__init__(edad , color)
        self.altura_maxima = altura_maxima

    def hablar(self): # SObrerescribio el metodo hablar de la clase padre
        print('Pio')

    def volar(self , metros):
        print(f"El pajaro vuelva {metros} metros")

piolin = Pajaro( 3 , "amarillo")
piolin.nacer()
piolin.hablar()
piolin.volar(10)