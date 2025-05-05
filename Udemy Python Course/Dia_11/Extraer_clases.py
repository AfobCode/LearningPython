import bs4
import requests

respuesta = requests.get("https://escueladirecta-blog.blogspot.com/2021/10/encapsulamiento-pilares-de-la.html")
texto_web = bs4.BeautifulSoup(respuesta.text, 'lxml')

columna_lateral = texto_web.select("#PopularPosts1 .item-content div")
print(columna_lateral)
########### Seleccionar info de la columna lateral
print("-"*60)
print(columna_lateral[2])

########### Seleccionar solo el texto sin etiquetas
print("-"*60)
print(columna_lateral[2].getText().strip())
