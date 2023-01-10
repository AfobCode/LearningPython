monedas = 5;

while monedas > 0:
    print(f"Tengo {monedas} monedas")
    monedas -=1
else:
    print("Saldo insuficiente")

#################################
# Loop While
# Se usa cuando no tengo control sobre el
# numero de iteraciones, y va depender del comportamiento
# del usuario/funcion
respuesta = 's'

while respuesta == 's':
    respuesta = input("Quieres seguir? (s/n)")
else:
    print("Gracias")

#################################
respuesta = 's'

#while respuesta == 's':
#    pass # salta la iteracion

print("hola")

#################################
#Break
for i in range(10):
    if (i % 2 != 0) and (i > 5):
        break # Interrumpe el loop, cuando ejecute esta linea termina el loop
    else:
        print(i)

print("Paso".center(20,"*"))
#################################
#Continue

for i in range(10):
    if i%2 == 0:
        continue # No rompe el loop pero salta esta iteracion y arranca la siguiente
    else:
        print(i)