from random import randint
from TDA_Cola import Cola
Cola_A = Cola()
Cola_B = Cola()

def cargar_colas(A,B):
    for i in range (0,10):
        if (i % 2 == 0):
            A.arribo(i)
        else:
            B.arribo(i)

def barrido_Colas(A,B):
    print("Cola A:")

    for i in range(0,A.tamanio()):
        print(A.move_end())

    print ("Cola B:")

    for i in range(0,B.tamanio()):
        print(B.move_end())

cargar_colas(Cola_A,Cola_B)

barrido_Colas(Cola_A, Cola_B)

print("Colas Cargadas...")

while not Cola_B.cola_vacia():
    valorB=Cola_B.atencion()
    valorA=Cola_A.atencion()
    if (valorB>=valorA):
        Cola_A.arribo(valorA)
        Cola_A.arribo(valorB)


print ("Fin")

barrido_Colas(Cola_A,Cola_B)