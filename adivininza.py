import random


def juego_adivinanza ():
    print("Bienvenido al juego de adivinanza")
    print('''El juego consiste en que el usuario tenga que 
          adivinar un número entre 1 y 20, 
          el cual será generado de manera aleatoria por el programa''')
    print("El usuario tendrá 5 intentos para adivinar el número")
    numero_secreto = random.randint(1, 20)
    intentos = 5

    while intentos > 0:
        print(f"Intentos restantes: {intentos}")
        numero_usuario = input("Ingrese un número entre 1 y 20: ")
        if numero_usuario.isdigit():
            numero_usuario = int(numero_usuario)
            intentos -= 1
            if numero_usuario < 1 or numero_usuario > 20:
                print("El número ingresado no está dentro del rango permitido")
            elif numero_usuario < numero_secreto:
                print("El número ingresado es menor que el número secreto")
            elif numero_usuario > numero_secreto:
                print("El número ingresado es mayor que el número secreto")
            else:
                print(f"¡Felicidades! Has adivinado el número secreto: {numero_secreto}")
        else:
            print("El número ingresado no es un número entero")
    

    if intentos == 0:
        print(f"Lo siento, no has podido adivinar el número secreto:{numero_secreto}")
        print("Gracias por jugar")

juego_adivinanza()
