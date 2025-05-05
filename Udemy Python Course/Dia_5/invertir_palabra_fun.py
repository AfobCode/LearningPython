def invertir_palabra(palabra: str):
    palabra_lista = [letra for letra in palabra]
    palabra_lista.reverse()
    palabra_invertida = "".join(palabra_lista)

    return palabra_invertida.upper()


palabra = "python"

print(invertir_palabra(palabra))