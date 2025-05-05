class Vaca:

    #Definir el metodo constructor
    def __init__(self, nombre):
        self.nombre = nombre

    def hablar(self):
        print("Muuu")


class Oveja:
    def __init__(self, nombre):
        self.nombre = nombre

    def hablar(self):
        print("Beee")

vaca1 = Vaca('lola')
oveja1 = Oveja('Nube')

# Esto es lo mas basico sobre el polimorfismo, dos clases distintas, tiene un metodo
# con el mismo nombre .hablar() pero cada metodo ejecuta algo diferente.

vaca1.hablar()
oveja1.hablar()

#Si creo una lista con objetos de clases distintas, pero cada clase tiene el mismo metodo
# voy a porder irterar esa lista de objetos y cada objeto ejecutara el metodo que le corresponde
animales = [vaca1 , oveja1]

for animal in animales:
    animal.hablar()

def animal_habla(animal):
    return animal.hablar()

animal_habla(vaca1)
animal_habla(oveja1)