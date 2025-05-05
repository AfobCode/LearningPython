import bs4
import requests
from pathlib import Path

cursos_pagina_web = requests.get("https://escueladirecta.com/courses")
sopa = bs4.BeautifulSoup(cursos_pagina_web.text , 'lxml')

imagenes = sopa.select('.course-box-image')

for i in range(len(imagenes)):
    foto = imagenes[i]['src']
    foto_bin = requests.get(foto)
    nombre_file = f"foto_descargada_{i}.jpg"
    file = open(Path('FotosScrapping',nombre_file),"wb") #el archivo se escribe de forma binaria
    file.write(foto_bin.content) #El content me trae toda la informacion en binario
    file.close()

