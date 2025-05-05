serie = "N-02"

if serie == "N-01":
    print("Samsung")
elif serie == "N-02":
    print("Nokia")
elif serie == "N-03":
    print("Motorola")
else:
    print("Referencia invalida")
############################################
match serie:
    case "N-01":
        print("Samsung")
    case "N-02":
        print("Nokia")
    case "N-03":
        print("Motorola")
    case _:
        print("Referencia invalida")

############################################
cliente = {
    'nombre':'Andres',
    'edad':25,
    'ocupacion':MC
}

pelicula = {
    'titulo': 'Avatar II',
    'ficha_tecnica':{
        'duracion': 3,
        'director': 'James Cameron'
    }
}

elementos = [cliente,pelicula,'libro']

for e in elementos:
    match e:
        case {'nombre': nombre,
              'edad' : edad,
              'ocupacion': ocupacion}:
            print("Es un cliente")
            print(nombre,edad,ocupacion)
        case {'titulo':titulo,
              'ficha_tecnica':{'duracion':duracion,
                               'director': director}}:
            print('Es una pelicula')
            print(f"la pelicula {titulo} dura {duracion}")
        case _:
            print("No registro")