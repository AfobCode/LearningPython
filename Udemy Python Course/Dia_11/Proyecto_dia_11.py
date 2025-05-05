import bs4
import requests


url_base = "http://books.toscrape.com/catalogue/page-{}.html"
libros_4s = []  # Lista para almacenar libros de 4 o mas estrella


for i in range(1,51):
    pag = url_base.format(i) #generar url de la siguiente pag
    info_p = requests.get(pag)
    soup = bs4.BeautifulSoup(info_p.text , 'lxml' )
    libros = soup.select('.product_pod')


    for libro in libros:
        titulo = libro.h3.getText()
        estellas = libro.p['class'][-1]

        if (estellas == 'Five') or (estellas == 'Four'):
            libros_4s.append(titulo)

print(f'Despues del escaneo hay {len(libros_4s)} con cuatro o mas estrellas')
for libro_4s in libros_4s:
    print(libro_4s)