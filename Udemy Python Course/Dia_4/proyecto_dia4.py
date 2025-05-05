"""
El programa le va a preguntar al usuario su nombre, y luego le va a decir
algo así como “Bueno, Juan, he pensado un número entre 1 y 100, y tienes solo ocho intentos
para adivinar cuál crees que es el número”. Entonces, en cada intento el jugador dirá un
número y el programa puede responder cuatro cosas distintas:
 Si el número que dijo el usuario es menor a 1 o superior a 100, le va a decir que ha elegido
un número que no está permitido.
 Si el número que ha elegido el usuario es menor al que ha pensado el programa, le va a
decir que su respuesta es incorrecta y que ha elegido un número menor al número secreto.
 Si el usuario eligió un número mayor al número secreto, también se lo hará saber de la
misma manera.
 Y si el usuario acertó el número secreto, se le va a informar que ha ganado y cuántos
intentos le ha tomado.
"""
from random import randint

user_name = input("Ingresa tu nombre: ")
num = randint(1,100)
print(num)

print(f"Bueno {user_name}, he pensado un número entre 1 y 100, y tienes solo ocho intentos para adivinar.")

for i in range(8):
    guess = int(input("¿cuál crees que es el número?: "))
    if guess == num:
        print(f"Has Ganado {user_name}, te tomo {i+1} intentos adivinarlo")
        break
    elif (guess < 1) or (guess > 100):
        print(f"has elegido un número que no está permitido")
    elif guess < num:
        print("respuesta incorrecta!! Has elegido un número menor al número secreto.")
    else:
        print("respuesta incorrecta!! Has elegido un número mayor al número secreto.")

print("Fin del Juego")