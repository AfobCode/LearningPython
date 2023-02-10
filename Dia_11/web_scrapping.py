import bs4
import requests

respuesta = requests.get('https://www.tradingview.com')

print(respuesta, type(respuesta))
print(respuesta.text) ## este metodo me trae tod0 el codigo fuente de la pagina que consulte

organizar_respuesta = bs4.BeautifulSoup(respuesta.text,'lxml')

print(organizar_respuesta.select('h1'))