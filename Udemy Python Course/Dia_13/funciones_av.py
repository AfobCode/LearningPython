import datetime
import pyttsx3 as pyt
import speech_recognition as sr
import pywhatkit as pwk
import yfinance as yf
import pyjokes as pj
import webbrowser as wb
import wikipedia as wkp

"""
Construir un asistente de voz, como siri o como alexa
"""

#Escuchar el microfono y devolver el audio como texto
def trasnformar_audio_texto():

    # almacenar recognizer en una variable
    r = sr.Recognizer()

    # configurar el microfono
    with sr.Microphone() as origen:

        # tiempo de espera
        r.pause_threshold = 0.8

        # informar inicio de grabacion
        print("Ya se puede hablar")

        #Guardar el audio capturado
        audio = r.listen(origen)

        try:
            # buscar en google
            pedido = r.recognize_google(audio , language="es-col")
            
            # prueba de que funciona
            print("Dijiste: " + pedido)

            #devolver transcripcion
            return pedido
        except sr.UnknownValueError:
            
            # No comprendio la info
            print("No entendi ni mierda")

            return "Sigo esperando"
        
        except sr.RequestError:
            # No comprendio la info
            print("No jodaaa! ")

            return "Sigo esperando"

        except:
            # No comprendio la info
            print("No vales monda")

            return "Sigo esperando"

def hablar(mensaje:str, voz_tipo):

    #encender el motor de pyttsx3
    engine = pyt.init()
    engine.setProperty('voice',voz_tipo)
    
    #pronunciar el mensaje
    engine.say(mensaje)
    engine.runAndWait()

def pedir_dia():
    dia = datetime.date.today()
    print(dia)

    # Crear variable con el dia de la semana
    dia_semana = dia.weekday()
    print(dia_semana)

    dia_semana_f = dia.strftime("%A")

    # diccionario con nombre de los dias
    calendario = {
        0:"Lunes",
        1:"Martes",
        2:"Miércoles",
        3:"Jueves",
        4:"Viernes",
        5:"Sábado",
        6:"Domingo"
    }

    print(calendario[dia_semana])
    print(dia_semana_f)

    # Decir dia de la semana
    hablar(f"Hoy es: {calendario[dia_semana]}",voces_id[0])
    hablar(f"Today: {dia_semana_f}",voces_id[1])

def pedir_hora():

    hora = datetime.datetime.now()
    print(hora)

    hablar(f"Son las {hora.hour} con {hora.minute} minutos", voces_id[0])

    time = datetime.datetime.now().strftime("%H:%M %p")
    print(time)

    hablar(f"It is {time}",voces_id[1])

def saludo_inicio():

    hora = datetime.datetime.now()
    if hora.hour < 6 or hora.hour > 19:
        momento = 'Buenas noches'
    elif hora.hour >= 6 and hora.hour < 12:
        momento = "Buenos Dias"
    else:
        momento = "Buenas tarder"

    #Decir el saludo
    hablar(f'Hola bebee, {momento}, soy tu AV. Por favor, dime en que te puedo ayudar', voces_id[0])

def pedir_cosas():

    #saludo inicial
    saludo_inicio()

    #Variable de corte
    comenzar = True

    while comenzar:
        peticion = trasnformar_audio_texto()
        despedidas = ['salir','chao','nos vemos','fin', 'adios']
        repositorios = ['repo','repositorio','repositorios','github']

        print(peticion)

        if peticion.lower()  in despedidas:
            hablar('Chao mor', voces_id[0])
            break
        elif peticion.lower() in repositorios:

            hablar('Va a estudiar mor?, que juicio bebe', voces_id[0])
            wb.open("https://github.com/AfobCode/LearningPython")
        
        elif 'busca en wikipedia' in peticion.lower():

            hablar('Buscando mor', voces_id[0])
            print(peticion)
            peticion = peticion.replace('busca en wikipedia', '') # quito el comando para que la peticion tenga solo el concepto
            
            wkp.set_lang('es')
            respuesta = wkp.summary(peticion, sentences=1)
            hablar('Vea lo que encontre mor', voces_id[0])
            hablar(respuesta, voces_id[0])
            print(peticion)
        
        elif 'busca en internet' in peticion.lower():

            hablar('Buscando bebéé', voces_id[0])
            print(peticion)
            peticion = peticion.replace('busca en internet', '') # quito el comando para que la peticion tenga solo el concepto
            pwk.search(peticion)
            hablar('Vea lo que encontre mor', voces_id[0])
        
        elif 'quiero escuchar' in peticion.lower() or 'reproducir' in peticion.lower() :

            hablar('Esoooo', voces_id[0])
            print(peticion)
            pwk.playonyt(peticion)
        
        elif 'broma' in peticion.lower() or 'chiste' in peticion.lower():

            hablar(pj.get_joke('es'), voces_id[0])
            hablar(pj.get_joke('en'), voces_id[1])
            hablar(pj.get_joke('it'), voces_id[0])

        elif 'precio de' in peticion.lower():

            accion = peticion.lower().split('de')[-1].strip()
            cartera = {"apple":'APPL',
                        'amazon':'AMZN',
                        'google':"GOOGL",
                        'tesla':"TSLA"}
            
            try:
                accion_buscada = cartera[accion]
                accion_buscada = yf.Ticker(accion_buscada)
                precio = accion_buscada.info['regularMarketPrice']
                hablar(f"El precio de {accion} es de {precio}, morcito", voces_id[1])
            except:
                hablar(f"no bebe, esa accion de {accion}, no la encontre", voces_id[1])

        elif 'qué hora es' in peticion.lower():
            pedir_hora()
        elif 'qué día es'  in peticion.lower() :
            pedir_dia()
        else:
            hablar(peticion,voces_id[0])

# Opciones de voz
engine = pyt.init()
voces_id = []
for voz in engine.getProperty('voices'):
    voces_id.append(voz.id)

pedir_cosas()