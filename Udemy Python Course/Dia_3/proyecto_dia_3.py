#La consigna es la siguiente: vas a crear un programa que primero le pida al usuario que
#ingrese un texto. Puede ser un texto cualquiera: un artículo entero, un párrafo, una frase, un
#poema, lo que quiera. Luego, el programa le va a pedir al usuario que también ingrese tres
#letras a su elección y a partir de ese momento nuestro código va a procesar esa información
#para hacer cinco tipos de análisis y devolverle al usuario la siguiente información:

# 1. Primero: ¿cuántas veces aparece cada una de las letras que eligió?
# 2. Segundo: le vas a decir al usuario cuántas palabras hay a lo largo de todo el texto
# 3. Tercero: nos va a informar cuál es la primera letra del texto y cuál es la última.
# 4. Cuarto: el sistema nos va a mostrar cómo quedaría el texto si invirtiéramos el orden de las palabras.
# 5. Quinto: el sistema nos va a decir si la palabra “Python” se encuentra dentro del texto.

txt = input("Por favor ingrese el texto: ")
txt_minusculas = txt.lower()
txt_lista = txt.split(" ")
letras = {}

# 1. Primero
for i in range(3):
    l = input(f"Ingrese la letra {i+1}: ")
    letras[l] = txt_minusculas.count(l)

# 2. Segundo
contar_palabras = len(txt_lista)


# 3. Tercero
primera_Letra , ultima_Letra = txt[0] , txt[-1]

#4. Cuarto:
txt_invertido = txt_lista
txt_invertido.reverse()
txt_invertido = " ".join(txt_invertido)

# 5. Quinto
p = "python" in txt_minusculas
if p:
    p = 'Si'
else:
    p = 'No'

respuesta = f"""
1. Cada letra se encontro tantas veces en su texto{letras}.
2. EL texto ingresado tiene en total {contar_palabras} palabras.
3. La primera letra de su texto es "{primera_Letra}" y la ultima es "{ultima_Letra}".
4. Si se invirtiera el texto obtendria algo asi:
\t '{txt_invertido}'
5. La palabra "Python" {p} esta en el texto
"""

print(respuesta)