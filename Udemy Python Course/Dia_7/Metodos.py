class Pajaro:

    #Atributos de clase
    alas = True
    pico = True

    #Metodo Constructor
    def __init__(self, color , especie):
        self.color = color #Atributos de instancia
        self.especie = especie # Atributo de instancia

    #Declaracion de metodos

    #Metodo piar
    def piar(self):
        print('Pio')

    #Metodo volar
    def volar(self , metros):
        print(f"El pajaro volo {metros}")

    #Metodo mostrar color
    def mostrar_color(self):
        print(f"Soy de color {self.color}")

piolin = Pajaro('Amarillo' , 'Canario')

piolin.piar()
piolin.volar(35)
piolin.mostrar_color()
