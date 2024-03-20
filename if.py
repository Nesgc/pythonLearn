from random import *
name= input("Cual es tu nombre: ")
print(f"Bueno {name} he pensando en un numero entre 1 y 100, y tienes solo ocho intentos para adivinar cuál crees que es el número")

aleatorio = randint(1,100)
intentos=0
print(aleatorio)

while True:
    respuesta = input("Dime un numero entre el 1 y el 100")
    respuesta = int(respuesta)

    if respuesta == aleatorio:
        print("felicidades lo adivinaste")
        break
    elif respuesta > 100 or respuesta < 1:

        intentos=+1
        print(f"elegiste un nuermo no permitido, te quedan {4-intentos}")
        if intentos > 3:
            print("se te acabaron los intentos")
            break
    elif respuesta > aleatorio:
        intentos+=1
        print(f"tu numero es mayor al aleatorio, te quedan {4-intentos}")

        if intentos > 3:
            print("se te acabaron los intentos")
            break
    elif respuesta < aleatorio:
        intentos += 1
        print(f"tu numero es menor al aleatorio, te quedan {4-intentos}")
        if intentos > 3:
            print("se te acabaron los intentos")
            break



