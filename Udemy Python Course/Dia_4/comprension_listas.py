palabra = "python"

lista = []
for l in palabra:
    lista.append(l)

print(lista)

lista_comp = [letra for letra in palabra]
print(lista_comp)


lista_num = [n for n in range(0,11,2)]
print(lista_num)

lista_opt = [n**2 for n in range(0,21,5)]
print(lista_opt)

####################################
#Una lista con la medida en pies, y yo la quiero en metros
pies = [10,20,30,40,50]
metros = [(n , n *3.281) for n in pies ]
print(metros)
