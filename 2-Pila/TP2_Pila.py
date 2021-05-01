from TDA_Pila import pila
from random import randint

def ocurrencias(buscado):
    element = pila()
    elementos_aux = pila()

    element.apilar(randint(0, 10))
    element.apilar(randint(0, 10))
    element.apilar(randint(0, 10))
    element.apilar(randint(0, 10))
    element.apilar(randint(0, 10))
    element.barrido_pila()
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
    nums.apilar(randint(0, 10))
    nums.apilar(randint(0, 10))
    nums.apilar(randint(0, 10))
    nums.apilar(randint(0, 10))
    nums.apilar(randint(0, 10))
    nums.barrido_pila()

    while(not nums.pila_vacia()):
        num = nums.desapilar()
        if (num % 2 == 0):
            aux.apilar(num)

    while(not aux.pila_vacia()):
        num = aux.desapilar()
        nums.apilar(num)

    nums.barrido_pila()















#buscado = int(input("ingresa algo wey: "))
#ocurrencias(buscado)
#eliminar_pares()