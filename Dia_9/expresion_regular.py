"""
Un uso practico para las expresiones regulares
es por ejemplo verificar que una clave cumple con ciertos
paramentros:
- No empieza con un numero, solo con una letra
- Tiene 8 caracteres
"""
import re

clave = input('Clave: ')
patron = r'\D{1}\w{7}'

chequear = re.search(patron , clave)
print(chequear)

################################
### Operadores especiales ######

texto = "No atendemos los lunes por la tarde."

# Operador "ó" se marca con |

buscar = re.search('Lunes|lunes', texto) #Va a buscar si Lunes esta o si esta lunes
print(buscar)

# Comdin . el operador . toma cualquier valor

buscar = re.search('..dem...', texto) #va a retormar dos caracteres cualesquiera que sean antes de "dem" y tres caracteres cualesquiera que sean despues.
print(buscar)

# Saber si un patron inicia con un cacaracter ^
buscar = re.findall(r'^\D*', texto) #Va a encontrar si el texto no empieza con un valor numerico
print(buscar)

# Saber si un patron finaliza con un caracter $
buscar = re.findall(r'\.$', texto) #revisa si el texto termina con un punto o no
print(buscar)

# Para indicar que no tome en cuenta algo [^] excluir
textico = "Soy andres y tengo 25 años"
buscar = re.findall(r'[^\d]+', textico) # excluye todos los numeros que encuentre
print(buscar)