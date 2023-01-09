#Proyecto 2
#La situación es esta: tú trabajas en una empresa donde los vendedores reciben comisiones
#del 13% por sus ventas totales, y tu jefe quiere que ayudes a los vendedores a calcular sus
#comisiones creando un programa que les pregunte su nombre y cuánto han vendido en este
#mes. Tu programa le va a responder con una frase que incluya su nombre y el monto que le
#corresponde por las comisiones.

nombre_empleado = input("Cual es tu nombre: ")
ventas_totales = int(input("Cuanto vendiste en total este mes: "))

comisiones = ventas_totales * 0.13
comisiones = round(comisiones,2)

respuesta = f"Hola {nombre_empleado}, felicitaciones tu comision es de: {comisiones}"
print(respuesta)