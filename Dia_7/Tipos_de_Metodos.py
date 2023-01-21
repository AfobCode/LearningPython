#Decoradores

#Metodos de instancia
# Son los metodos comunes que se declaran como un funcion def metodo(self):
# Estos pueden acceder y modificar atributos de un objeto
# pueden acceder a otros metodos
# pueden modificar el estado de la clase

#Metodos de clase @classmethod
# Se usa el decorador @classmethod ante de definir la funcion y se define def metodo(cls):
# Estos metodos no estan asociados a la instanci a u objeto, estan asociados a la clase como tal
# de tal manera que pueden ser llamados desde la clase
# Pueden modificar los atributos de la clase

#Metodos estaticos @staticmethod
# Se usa el decorador @staticmethod ante de definir la funcion y se define def metodo():
# No pueden modificar el estado ni de la clase ni de la instancia
# Pero si pueden aceptar parametros de entrada

class Pajaro:

    #Atributos de clase
    alas = True
    pico = True

    #Metodo Constructor
    def __init__(self, color , especie):
        self.color = color #Atributos de instancia
        self.especie = especie # Atributo de instancia

    #Declaracion de metodos
    # *************************************
    #Metodos de instancia, sirven para modificar los objetos
    #Metodo piar
    def piar(self):
        print('Pio')

    #Metodo volar
    def volar(self , metros):
        print(f"El pajaro volo {metros}")
        self.piar() #desde el metodo volar, llamo al metodo de instancia piar para que se ejecute

    #Metodo mostrar color
    def mostrar_color(self):
        print(f"Soy de color {self.color}")
    #*************************************

    # *************************************
    #Metodos de Clase, usan el decorador @classmethod => def metodo(cls):
    @classmethod
    def poner_huevos(cls , cantidad):
        print(f"Puso {cantidad} huevos")

    @classmethod
    def numero_alas(cls):
        cls.alas = 2 #Puedo modificar atributos de clase, pero no de instancia
    # *************************************

    # *************************************
    # Metodos estaticos, usan el decorador @staticmethod => def metodo():
    # Estos metodos no pueden modificar ni la clase ni las instancias

    @staticmethod
    def mirar():
        print("El pajaro mira")





# Crear dos instancias de clase Pajaro
piolin = Pajaro('Amarillo' , 'Canario')
twitter = Pajaro('Azul cielo' , 'Canario')

# Utilizar metodos de instancia
piolin.volar(10) # el metodo volar llama y accede al metodo piar
piolin.alas = False # Cambio el valor de alas que es un atributo de clase pero solo para el objeto piolin
print(piolin.alas , twitter.alas)

# Utilizar metodos de clase
Pajaro.poner_huevos(3) # No tuve que llamar a una instancia, directamente desde la clase
piolin.poner_huevos(2) # Igualemente lo puedo llamar desde la instancia
print(piolin.alas , twitter.alas , type(Pajaro.alas)) #Es un booleano
Pajaro.numero_alas() # Llamo al metodo de clase, que modifica el atributo de clase
print(piolin.alas , twitter.alas , type(Pajaro.alas)) # Piolin sigue siendo False porque los metodos de clase no pueden modificar a las instancias
                                                        # en la linea 70 se declaro que para la instancia piolin el atributo alas es False

# Utilizar metodos estaticos
Pajaro.mirar()
twitter.mirar()