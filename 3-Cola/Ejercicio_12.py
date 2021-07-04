from Ejercicio_11 import barrido_cola
from random import randint
from TDA_Cola import Cola
Cola_A = Cola()
Cola_B = Cola()

def cargar_Colas(A,B): #Carga de valores random a las Colas
    Arr=[]
    for i in range(0,10):
        Arr.append(randint(0,10))
    Arr.sort()

    for i in range(0,10):
        A.arribo(Arr.pop(0))

    Arr=[]
    for i in range(0,10):
        Arr.append(randint(0,10))
    Arr.sort()

    for i in range(0,10):
        B.arribo(Arr.pop(0))

def barrido_Colas(A,B): #solo para probar "cosas"
    print("Cola A:")

    for i in range(0,A.tamanio()-1):
        print(A.move_end())

    print ("Cola B:")

    for i in range(0,B.tamanio()-1):
        print(B.move_end())


cargar_Colas(Cola_A, Cola_B)
#barrido_Colas(Cola_A,Cola_B)
