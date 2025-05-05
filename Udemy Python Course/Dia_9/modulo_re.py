"""
Expresiones regulares
"""
import re
texto = "Si necesitas ayuda llama al (658)-598-9977 las 24 horas al servicio de ayuda online"
palabra = 'ayuda' in texto
print(palabra)

patron = 'nada'
busqueda = re.search(patron,texto)
print(busqueda)

patron = 'necesitas'
busqueda = re.search(patron,texto)
print(busqueda)
print(busqueda.span())
print(busqueda.start())
print(busqueda.end())

patron = 'ayuda'
busqueda = re.findall(patron,texto)
print(busqueda)
print(len(busqueda))

for palabra in re.finditer(patron, texto):
    print(palabra.span())

texto2 = "llama al 564-525-6588 ya mismo"

patron = r'\d\d\d-\d\d\d-\d\d\d\d'
resultado = re.search(patron, texto2)
print(resultado.group())

patron2 = r'\d{3}-\d{3}-\d{4}'

#puedo compilar los patrones de busqueda
# y encerrarlos en parentesis para luego dirigirme a un patron en particular

patron_compilado = re.compile(r'(\d{3})-(\d{3})-(\d{4})')
resultado = re.search(patron_compilado,texto2)
print(resultado.group(3)) # Como en el patron_compildado tengo tres grupos encerrados en parentesis, aca me da a devolver al ultimo grupo, el tercero
