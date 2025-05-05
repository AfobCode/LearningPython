class CD:

    def __init__(self , autor , titulo, canciones):
        self.autor = autor
        self.titulo = titulo
        self.canciones = canciones

    def __str__(self): #defino como quiero que mi clase se muestre cuando sea llamado por la funcion print()
        return f"Album: {self.titulo} de {self.autor}"

    def __len__(self): #Defino como quiero que mi clase se comporte cuando lo llama la funcion len()
        return self.canciones

    def __del__(self): #Agrego f
        print("Se ha eliminado un CD")

mi_cd = CD('Pink Floyd', 'The Wall', 24)