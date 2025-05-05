import tkinter
import random
import datetime
import pathlib 
from tkinter import filedialog, messagebox

operador = ''

# Listado de precios
precios_comida = [1.32,1.65,2.31,3.22,1.22]
precios_bebida = [0.25,0.99,1.21,1.54,1.08]
precios_postre = [1.54,1.68,1.32,1.97,2.55]

def click_boton(boton_precionado):
    global operador

    try:
        int(boton_precionado)
        numero = True
    except:
        numero = False

    if numero:
        operador += boton_precionado
    else:
        operador += ' ' + boton_precionado + ' '

    visor_calculadora.delete(0,'end')
    visor_calculadora.insert('end',operador)

def borrar():
    global operador
    operador = ''
    visor_calculadora.delete(0, 'end')

def obtener_resultado():

    global operador

    operacion = operador.split(' ')
    numeros = []
    signos = []

    for valor in operacion:
        if len(valor) > 0:
            try:
                numero = float(valor)
                numeros.append(numero)
            except:
                signos.append(valor)

    resultado = numeros.pop(0)

    while len(numeros) > 0:
        signo = signos.pop(0)
        n = numeros.pop(0)

        if signo == '+':
            resultado += n
        elif signo == '-':
            resultado -= n
        elif signo == '*':
            resultado *= n
        elif signo == '/':
            resultado /= n

    visor_calculadora.delete(0, 'end')
    visor_calculadora.insert('end', resultado)
    operador = f'{resultado}'

def revisar_check():
    #*******************************
    # Comidas
    x = 0
    for c in cuadros_comidas:
        if variables_comida[x].get() == 1:

            cuadros_comidas[x].config(state='normal')
            cuadros_comidas[x].focus()

            if cuadros_comidas[x].get() == '0':
                cuadros_comidas[x].delete(0,'end')

        elif variables_comida[x].get() == 0:
            cuadros_comidas[x].config(state='disable')
            texto_comidas[x].set('0')

        x += 1
    # *******************************
    # bebidas
    x = 0
    for c in cuadros_bebidas:
        if variables_bebida[x].get() == 1:

            cuadros_bebidas[x].config(state='normal')
            cuadros_bebidas[x].focus()

            if cuadros_bebidas[x].get() == '0':
                cuadros_bebidas[x].delete(0,'end')

        elif variables_bebida[x].get() == 0:
            cuadros_bebidas[x].config(state='disable')
            texto_bebidas[x].set('0')

        x += 1


    # *******************************
    # postres
    x = 0
    for c in cuadros_postres:
        if variables_postre[x].get() == 1:

            cuadros_postres[x].config(state='normal')
            cuadros_postres[x].focus()

            if cuadros_postres[x].get() == '0':
                cuadros_postres[x].delete(0,'end')

        elif variables_postre[x].get() == 0:
            cuadros_postres[x].config(state='disable')
            texto_postres[x].set('0')

        x += 1

def total():

    #Comidas
    sub_total_comida = 0
    p = 0
    for cantidad in texto_comidas:
        sub_total_comida += float(cantidad.get()) * precios_comida[p]
        p += 1
    #******************************
    # Bebidas
    sub_total_bebida = 0
    p = 0
    for cantidad in texto_bebidas:
        sub_total_bebida += float(cantidad.get()) * precios_bebida[p]
        p += 1

    # ******************************
    # Postres
    sub_total_postre = 0
    p = 0
    for cantidad in texto_postres:
        sub_total_postre += float(cantidad.get()) * precios_postre[p]
        p += 1

    var_comida_costos.set(f"$ {round(sub_total_comida, 2)}")
    var_bebida_costos.set(f"$ {round(sub_total_bebida, 2)}")
    var_postre_costos.set(f"$ {round(sub_total_postre, 2)}")

    sub_total = sub_total_comida + sub_total_bebida + sub_total_postre
    sub_impuestos = sub_total * 0.19
    total = sub_total + sub_impuestos

    var_subtotal.set(f"$ {round(sub_total,2)}")
    var_impuestos.set(f"$ {round(sub_impuestos,2)}")
    var_total.set(f"$ {round(total,2)}")

def reset():
    var_comida_costos.set('')
    var_bebida_costos.set('')
    var_postre_costos.set('')
    var_subtotal.set('')
    var_impuestos.set('')
    var_total.set('')
    texto_recibo.delete(1.0,'end')

    # Comidas
    x = 0
    for c in cuadros_comidas:
        variables_comida[x].set(0)
        cuadros_comidas[x].config(state='disable')
        texto_comidas[x].set(0)

        x += 1

    # Bebidas
    x = 0
    for c in cuadros_bebidas:
        variables_bebida[x].set(0)
        cuadros_bebidas[x].config(state='disable')
        texto_bebidas[x].set('0')

        x += 1

    # postres
    x = 0
    for c in cuadros_postres:
        variables_postre[x].set(0)
        cuadros_postres[x].config(state='disable')
        texto_postres[x].set('0')

        x += 1

def recibo():
    separador = "\n" + "*"*50 +"\n\n"
    texto_recibo.delete(1.0,'end')
    total()
    numero_recibo = f"N# - {random.randint(1000,9999)}"
    fecha = datetime.datetime.today().strftime("%d/%m/%y - %H:%M %p")
    x = 0
    platos = ''
    for c in cuadros_comidas:
        if variables_comida[x].get() == 1:
            platos += f"{lista_comidas[x]} ... ${precios_comida[x]} ({texto_comidas[x].get()})\n\t"

        x += 1

    x = 0
    bebidas = ''
    for c in cuadros_bebidas:
        if variables_bebida[x].get() == 1:
            bebidas += f"{lista_bebidas[x]} ... ${precios_bebida[x]} ({texto_bebidas[x].get()})\n\t"

        x += 1
    
    x = 0
    postres = ''
    for c in cuadros_postres:
        if variables_postre[x].get() == 1:
            postres += f"{lista_postres[x]} ... ${precios_postre[x]} ({texto_postres[x].get()})\n\t"

        x += 1


    factura_info = f"""
Datos Factura: {numero_recibo}\t{fecha}
    {separador}
    Comida:\t{var_comida_costos.get()}\n
        {platos}\n
    Bebida:\t{var_bebida_costos.get()}\n
        {bebidas}\n
    Postres:\t{var_postre_costos.get()}\n
        {postres}\n 
    {separador}
    Sub-Total:\t{var_subtotal.get()}\n
    Impuestos:\t{var_impuestos.get()} (19%)\n
Total:\t{var_total.get()}\n
    """

    texto_recibo.insert('end',factura_info)
    return factura_info

def guardar():
    compra_info = recibo()
    compra_info += '='*60 + "\n"
    historial = open('libro_de_ventas.txt','a')
    historial.write(compra_info)
    historial.close()
    messagebox.showinfo('Informacion','Su recibo ha sido guardado')

    


#Inicializar la ventana tipo tkinter
app = tkinter.Tk()

#establecer el tamaño de la ventana tkinter
app.geometry('1080x630+0+0')

# establecer el titulo de la ventana
app.title('Gestor del restaurante')

# cabiar el fondo de la ventana
app.config(bg='burlywood')
#########################################################
#Panel superior

panel_superior = tkinter.Frame(app, bd = 1, relief="flat")
panel_superior.pack(side="top")

#Etiqueta titulo
etiqueta_titulo = tkinter.Label(panel_superior,text='Gestor de restaurante' , fg ='azure4',
                                font=('Dosis', 38),bg = 'burlywood', width=28)

etiqueta_titulo.grid(row=0,column=0)
#########################################################
#Panel Izquierdo

panel_izquierdo = tkinter.Frame(app, bd = 1, relief="flat")
panel_izquierdo.pack(side="left")

#panel costos
panel_costos = tkinter.Frame(panel_izquierdo, bd= 1 , relief="flat", bg='Azure4', pady=10)
panel_costos.pack(side='bottom')

#panel comidas
panel_comidas= tkinter.LabelFrame(panel_izquierdo , text= 'Comida', font=('Dosis', 19, 'bold'), bd = 1, relief='flat', fg= 'azure4', pady= 20)
panel_comidas.pack(side = 'left')

#panel bebidas
panel_bebidas= tkinter.LabelFrame(panel_izquierdo , text= 'Bebidas', font=('Dosis', 19, 'bold'), bd = 1, relief='flat', fg= 'azure4', pady= 20)
panel_bebidas.pack(side = 'left')

#panel postres
panel_postres= tkinter.LabelFrame(panel_izquierdo , text= 'Postres', font=('Dosis', 19, 'bold'), bd = 1, relief='flat', fg= 'azure4', pady= 20)
panel_postres.pack(side = 'left')

#########################################################
#Panel Derecha
panel_derecha = tkinter.Frame(app, bd = 1, relief="flat")
panel_derecha.pack(side="right")

#panel calculadora
panel_calculadora = tkinter.Frame(panel_derecha, bd= 1 , relief="flat" , bg = 'burlywood')
panel_calculadora.pack(side='top')

#panel recibo
panel_recibo = tkinter.Frame(panel_derecha, bd= 1 , relief="flat" , bg = 'burlywood')
panel_recibo.pack(side='top')

#panel botones
panel_botones = tkinter.Frame(panel_derecha, bd= 1 , relief="flat" , bg = 'burlywood')
panel_botones.pack(side='top')

#########################################################
#Lista de productos
#[(comida, bebida, postre)]
lista_comidas = ['Hbg Queso' , "Hbg Tocineta" , 'Pizza Jamon' , 'Pizza Queso' , 'Perro']
lista_bebidas = ['Jugo Natural' ,  'Gaseosa' , 'Cerveza' , 'Vino' , 'agua']
lista_postres = ['Helado' , 'Brownie' , 'Arequipe' , 'postre' , 'Fruta']

# Agregar los productos en lista

#Generar items comida
variables_comida = []
cuadros_comidas = []
texto_comidas = []
contador = 0

for plato in lista_comidas:

    # Crear Checkbutton
    variables_comida.append('')
    variables_comida[contador] = tkinter.IntVar()

    plato = tkinter.Checkbutton(panel_comidas,
                                text=plato.title(),
                                font=('Dosis', 14 , 'bold'),
                                onvalue= 1,
                                offvalue= 0,
                                variable= variables_comida[contador],
                                command=revisar_check)

    plato.grid(row=contador,column=0, sticky='w')

    #crear los cuadros de entrada:
    cuadros_comidas.append('')
    texto_comidas.append('')
    texto_comidas[contador] = tkinter.StringVar()
    texto_comidas[contador].set(0)

    cuadros_comidas[contador] = tkinter.Entry(panel_comidas,
                                              font=('Dosis', 14 , 'bold'),
                                              bd=1,
                                              width=4,
                                              state='disabled',
                                              textvariable=texto_comidas[contador])

    cuadros_comidas[contador].grid(row=contador,column=1,sticky='w')

    contador += 1

#Generar items bebida
variables_bebida = []
cuadros_bebidas = []
texto_bebidas = []
contador = 0

for bebida in lista_bebidas:

    variables_bebida.append('')
    variables_bebida[contador] = tkinter.IntVar()

    #Crear checkbutton
    bebida = tkinter.Checkbutton(panel_bebidas,
                                 text = bebida.title(),
                                 font=('Dosis', 14 , 'bold'),
                                 onvalue= 1,
                                 offvalue= 0,
                                 variable= variables_bebida[contador],
                                 command=revisar_check)

    bebida.grid(row=contador,column=0, sticky='w')

    # crear los cuadros de entrada:
    cuadros_bebidas.append('')
    texto_bebidas.append('')
    texto_bebidas[contador] = tkinter.StringVar()
    texto_bebidas[contador].set(0)

    cuadros_bebidas[contador] = tkinter.Entry(panel_bebidas,
                                              font=('Dosis', 14, 'bold'),
                                              bd=1,
                                              width=4,
                                              state='disabled',
                                              textvariable=texto_bebidas[contador])

    cuadros_bebidas[contador].grid(row=contador, column=1, sticky='w')

    contador += 1

#Generar items postre
variables_postre = []
cuadros_postres = []
texto_postres = []
contador = 0

for postre in lista_postres:

    variables_postre.append('')
    variables_postre[contador] = tkinter.IntVar()

    # Crear checkbuttons
    postre = tkinter.Checkbutton(panel_postres,
                                 text = postre.title(),
                                 font=('Dosis', 14 , 'bold'),
                                 onvalue= 1,
                                 offvalue= 0,
                                 variable= variables_postre[contador],
                                 command=revisar_check)

    postre.grid(row=contador,column=0, sticky='w')

    # crear los cuadros de entrada:
    cuadros_postres.append('')
    texto_postres.append('')
    texto_postres[contador] = tkinter.StringVar()
    texto_postres[contador].set(0)

    cuadros_postres[contador] = tkinter.Entry(panel_postres,
                                              font=('Dosis', 14, 'bold'),
                                              bd=1,
                                              width=4,
                                              state='disabled',
                                              textvariable=texto_postres[contador])

    cuadros_postres[contador].grid(row=contador, column=1, sticky='w')

    contador += 1
#########################################################
#Variables
var_comida_costos = tkinter.StringVar()
var_postre_costos = tkinter.StringVar()
var_bebida_costos = tkinter.StringVar()
var_subtotal = tkinter.StringVar()
var_impuestos = tkinter.StringVar()
var_total = tkinter.StringVar()

# Etiquetas de costos y campos de entrada
etiqueta_costo_comida = tkinter.Label(panel_costos,
                                      text='Valor de la comida',
                                      font=('Dosis',14,'bold'),
                                      bg='azure4',
                                      fg = 'white')

etiqueta_costo_comida.grid(row=0,column=0)

texto_costo_comida = tkinter.Entry(panel_costos,
                                    bd=1,
                                    width=10,
                                    state='readonly',
                                    textvariable=var_comida_costos)

texto_costo_comida.grid(row=0,column=1, padx= 36)

#*******************************
etiqueta_costo_bebida = tkinter.Label(panel_costos,
                                      text='Valor de la bebida',
                                      font=('Dosis',14,'bold'),
                                      bg='azure4',
                                      fg = 'white')

etiqueta_costo_bebida.grid(row=1,column=0)

texto_costo_bebida = tkinter.Entry(panel_costos,
                                    bd=1,
                                    width=10,
                                    state='readonly',
                                    textvariable=var_bebida_costos)

texto_costo_bebida.grid(row=1,column=1, padx= 36)

#*******************************
etiqueta_costo_postre = tkinter.Label(panel_costos,
                                      text='Valor de los postres',
                                      font=('Dosis',14,'bold'),
                                      bg='azure4',
                                      fg = 'white')

etiqueta_costo_postre.grid(row=2,column=0)

texto_costo_postre = tkinter.Entry(panel_costos,
                                    bd=1,
                                    width=10,
                                    state='readonly',
                                    textvariable=var_postre_costos)

texto_costo_postre.grid(row=2,column=1, padx= 36)
#*******************************
etiqueta_subtotal = tkinter.Label(panel_costos,
                                      text='Valor Subtotal',
                                      font=('Dosis',14,'bold'),
                                      bg='azure4',
                                      fg = 'white')

etiqueta_subtotal.grid(row=0,column=2)

texto_subtotal = tkinter.Entry(panel_costos,
                                    bd=1,
                                    width=10,
                                    state='readonly',
                                    textvariable=var_subtotal)

texto_subtotal.grid(row=0,column=3, padx= 36)

#*******************************
etiqueta_impuestos = tkinter.Label(panel_costos,
                                      text='Valor impuestos',
                                      font=('Dosis',14,'bold'),
                                      bg='azure4',
                                      fg = 'white')

etiqueta_impuestos.grid(row=1,column=2)

texto_impuestos = tkinter.Entry(panel_costos,
                                    bd=1,
                                    width=10,
                                    state='readonly',
                                    textvariable=var_impuestos)

texto_impuestos.grid(row=1,column=3, padx= 36)

#*******************************
etiqueta_total = tkinter.Label(panel_costos,
                                      text='Valor total',
                                      font=('Dosis',14,'bold'),
                                      bg='azure4',
                                      fg = 'white')

etiqueta_total.grid(row=2,column=2)

texto_total = tkinter.Entry(panel_costos,
                                    bd=1,
                                    width=10,
                                    state='readonly',
                                    textvariable=var_total)

texto_total.grid(row=2,column=3, padx= 36)
#########################################################
# Crear y mostrar los botones en su panel
# Botones

botones = ['Total', 'Recibo' , 'Guardar' , 'Borrar']
botones_creados = []
columnas = 0

for boton in botones:
    boton = tkinter.Button(panel_botones,
                           text=boton.title(),
                           font=('Dosis', 10 , 'bold'),
                           fg= 'white',
                           bg = 'Azure4',
                           bd=1,
                           width= 10,
                           padx= 10
    )

    botones_creados.append(boton)

    boton.grid(row=0,column=columnas)
    columnas += 1

botones_creados[0].config(command=total)
botones_creados[1].config(command=recibo)
botones_creados[2].config(command=guardar)
botones_creados[-1].config(command=reset)
#########################################################
#Area de Recibo
texto_recibo = tkinter.Text(panel_recibo,
                            font=('Dosis',12,'bold'),
                            bd=1,
                            width=42,
                            height=10)

texto_recibo.grid(row=0,column=0)
#########################################################
# Calculadora

visor_calculadora = tkinter.Entry(panel_calculadora,
                                  font=('Dosis', 16 , 'bold'),
                                  width=32,
                                  bd =1)

visor_calculadora.grid(row=0,
                       column=0,
                       columnspan = 4)

# Agrear los botones a la calculadora
botones_calculadora = ['7','8','9','+','4','5','6','-',
                       '1','2','3','x','CE','BORRAR','0','/']

botones_guardados = []
columnas = 0
filas = 1
for boton in botones_calculadora:
    boton = tkinter.Button(panel_calculadora,
                           text=boton.title(),
                           font=('Dosis', 12 , 'bold'),
                           fg= 'white',
                           bg = 'Azure4',
                           bd=1,
                           width= 10
    )

    botones_guardados.append(boton)

    boton.grid(row=filas,column=columnas)
    columnas += 1

    if columnas > 3:
        filas += 1
        columnas = 0



botones_guardados[11].config(command=lambda: click_boton('*'))
botones_guardados[0].config(command=lambda : click_boton('7'))
botones_guardados[1].config(command=lambda : click_boton('8'))
botones_guardados[2].config(command=lambda : click_boton('9'))
botones_guardados[3].config(command=lambda : click_boton('+'))
botones_guardados[4].config(command=lambda : click_boton('4'))
botones_guardados[5].config(command=lambda : click_boton('5'))
botones_guardados[6].config(command=lambda : click_boton('6'))
botones_guardados[7].config(command=lambda : click_boton('-'))
botones_guardados[8].config(command=lambda : click_boton('1'))
botones_guardados[9].config(command=lambda : click_boton('2'))
botones_guardados[10].config(command=lambda : click_boton('3'))
botones_guardados[14].config(command=lambda : click_boton('0'))
botones_guardados[15].config(command=lambda : click_boton('/'))

botones_guardados[13].config(command=borrar)
botones_guardados[12].config(command=obtener_resultado)

#########################################################
# Evitar que el usuario pueda maximizar la ventana
app.resizable(0,0)

# Evitar que la ventana se cierre
app.mainloop()

