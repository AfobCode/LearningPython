mi_bool = 4 < 5 < 6
print(mi_bool)

#Comparador logico "Y"
mi_bool = (4 < 5) and (5 > 6)
print(mi_bool)

mi_bool = (55 <= 55.00) and ('Blanco'.lower() > 'blanco')
print(mi_bool)

#Comparador logico "O"
mi_bool = ('perro' == 'Animal') or (7 > 6)
print(mi_bool)

txt = "esta frasa es breve"
mi_bool = ('frase' in txt ) and ('Python' in txt)
print(mi_bool)

mi_bool = ('frase' in txt ) or ('Python' in txt)
print(mi_bool)

#Comparador logino "Not"
mi_bool = not (5 > 6)
print(mi_bool)
