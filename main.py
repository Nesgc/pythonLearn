
from statistics import median

def devolver_distintos(num1,num2,num3):

    suma=num1+num2+num3

    mayor=max(num1,num2,num3)
    menor=min(num1,num2,num3)
    media=median([num1,num2,num3])
    if suma > 15:
        print(mayor)
    elif suma < 10:
        print(menor)
    elif suma > 10 and suma < 15:
        print(media)

devolver_distintos(5,4,3)
