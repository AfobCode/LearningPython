def conteo_vidas():
    vidas = 4

    while vidas > 1:
        vidas -= 1
        if vidas == 1:
            yield f"Te queda {vidas} vida"
        else:
            yield f"Te quedan {vidas} vidas"

    yield "Game Over"

perder_vida = conteo_vidas()

print(next(perder_vida))
print(next(perder_vida))
print(next(perder_vida))
print(next(perder_vida))