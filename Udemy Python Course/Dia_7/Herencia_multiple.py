class Padre:
    def hablar(self):
        print("Hola Mijo")

class Madre:
    def reir(self):
      print("Jajaja que gonorrea")

    def hablar(self):
        print("Que paso mijito")

#Herencia Multiple, hereda de madre y de padre tambien
class Hijo(Padre , Madre): #Primero revisa metodos y atributos de la clase "Padre" y luego revisa los metodos y atributos de la clase "Madre"
    pass

#Hereda de todas las clases, Hijo , Padre, y Madre
class Nieto(Hijo):
    pass


nieto1 = Nieto()
nieto1.hablar() #Va a emplear el metodo #Hablar de la case "padre" ya que fue la primera clase que se le paso a la clase "Hijo"
nieto1.reir()

#Si quiero revisar cual sera el orden de ejecucion de la clase para buscar metodos y atributos
print(Nieto.mro())