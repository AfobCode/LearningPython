#atributos

#Atributos de clase:
# Es un atributo que todos los objetos van a tener y sera el mismo valor para todos
# por ejemplo, si la clase Pajaro, tiene un atributo alas = True
# todos los objetos de la clase Pajaro tendran el atributo alas = True

# #Atributos de instancia:
# Es un atributo que sera diferente para cada objeto/instancia de esa clase
# por ejemplo, si la clase Pajaro, tiene un atributo color
# cada objeto de la clase Pajaro tendra para el atributo color un valor diferente

class Pajaro:

    #Atributos de clase
    alas = True
    pico = True

    #Metodo Constructor
    def __init__(self, color , especie):
        self.color = color #Atributos de instancia
        self.especie = especie # Atributo de instancia



twitter = Pajaro('Azul' , 'Tucan')
piolin = Pajaro( 'Amario' , 'Canario')


print(f"El pajaro twitter es un {twitter.especie} y es de color {twitter.color}")
print(f"El pajaro piolin es un {piolin.especie} y es de color {piolin.color}")
# Aca llamo a dos atributos de cada objeto que al ser atributos de clase
# Van a ser iguales para los dos objetos y que no fue necesario asignarles un valor
# cuando cree la instancia.
print(f"Piolin tinee alas? {piolin.alas}\nTwitter tiene alas? {twitter.alas}")
print(f"Piolin tinee pico? {piolin.pico}\nTwitter tiene pico? {twitter.pico}")