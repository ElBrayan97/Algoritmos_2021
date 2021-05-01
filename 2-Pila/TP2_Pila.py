from TDA_Pila import pila
from random import randint

def cargar_pila_random(pila): # funcion para cargar elementos random a una pila
    pila.apilar(randint(0, 10))
    pila.apilar(randint(0, 10))
    pila.apilar(randint(0, 10))
    pila.apilar(randint(0, 10))
    pila.apilar(randint(0, 10))
    #pila.barrido_pila()

def ocurrencias(buscado):
    element = pila()
    elementos_aux = pila()
    cargar_pila_random(element)

    cont = 0
    while(not element.pila_vacia()):
        dato = element.desapilar()
        if (dato == buscado):
            cont += 1
        elementos_aux.apilar(dato)
    print("Elementos encontrados: ", cont)


def eliminar_pares():
    nums = pila()
    aux = pila()
    cargar_pila_random(nums)

    while(not nums.pila_vacia()):
        num = nums.desapilar()
        if (num % 2 == 0):
            aux.apilar(num)

    while(not aux.pila_vacia()):
        num = aux.desapilar()
        nums.apilar(num)

    #nums.barrido_pila()

def reemplazar(buscado, suplente):
    nums = pila()
    aux = pila()
    cargar_pila_random(nums)

    while (not nums.pila_vacia()):
        dato = nums.desapilar()
        if (dato == buscado):
            aux.apilar(suplente)
        else:
            aux.apilar(dato)

    while (not aux.pila_vacia()):
        dato = aux.desapilar()
        nums.apilar(dato)

    #nums.barrido_pila()













#buscado = int(input("ingresa algo wey: "))
#ocurrencias(buscado)
#eliminar_pares()
#reemplazar(3,5)
