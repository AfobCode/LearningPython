dic = {
    'c1': 100,
    'c2': 500
}
dic["last_element"] = 700
popped = dic.popitem() # Basado en la documentacion este metodo elimina
print(popped, dic)
############################
cleaned = ",:_#,,,,,,:::____##Pyt%on_ _Total,,,,,,::#".lstrip(',:%_#')
print(cleaned)
############################
frutas = ["mango", "banana", "cereza", "ciruela", "pomelo"]
frutas.insert(3,"naranja")
############################
marcas_smartphones = {"Samsung", "Xiaomi", "Apple", "Huawei", "LG"}
marcas_tv = {"Sony", "Philips"}#, "Samsung", "LG"}

print(marcas_smartphones.isdisjoint(marcas_tv))