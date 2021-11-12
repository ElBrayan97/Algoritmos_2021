from TDA_Lista import Lista
from random import randint


def cargar(L1, L2):
    for i in range (0, 10):
        L1.insertar(randint(10,100))
        L2.insertar(randint(10,100))
    """print ("Lista 1: ")
    L1.barrido()
    print ("Lista 2: ")
    L2.barrido()
"""

def concatenar(L1,L2): # Concatena las listas sin revisar los elementos
    while not L1.lista_vacia():
        num = L1.eliminar_primero()
        L2.insertar(num)


def concatenar_omitiendo(L1,L2): # Concatena las listas revisando los elementos
    while not L1.lista_vacia():
        num = L1.eliminar_primero()
        if L2.busqueda(num)== -1:
            L2.insertar(num)


def repetidos(L1,L2): # Contar los repetidos entre las 2 listas (intersecciones)
    cont=0
    while not L1.lista_vacia():
        num = L1.eliminar_primero()
        if L2.busqueda(num) != -1:
            cont+=1
    return (cont)


def eliminar(L1,L2): # Eliminar todos los elementos (nodos) de una lista
    while not L1.lista_vacia():
        print (L1.eliminar_primero())
    print ("Lista 1 Vacia")

Lista1 = Lista()
Lista2 = Lista()

cargar(Lista1, Lista2)
print ("fin de carga")
#concatenar(Lista1, Lista2) #A
#concatenar_omitiendo(Lista1,Lista2) #B
#print("Hay ",repetidos(Lista1,Lista2)," elementos repetidos") #C
#eliminar(Lista1, Lista2) #D