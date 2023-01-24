def multiplos_7():
    multiplicador = 0

    while multiplicador >= 0:
        multiplicador += 1
        yield multiplicador * 7

generador = multiplos_7()

print(next(generador))
print(next(generador))
print(next(generador))
print(next(generador))
print(next(generador))
print(next(generador))

