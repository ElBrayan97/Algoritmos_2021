from TDA_Pila import pila
from random import randint

def cargar_pila_random(pila): # funcion para cargar elementos random a una pila
    pila.apilar(randint(0, 10))
    pila.apilar(randint(0, 10))
    pila.apilar(randint(0, 10))
    pila.apilar(randint(0, 10))
    pila.apilar(randint(0, 10))
    #pila.barrido_pila()

def ocurrencias(buscado): # ok
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

def eliminar_pares(): # ok
    nums = pila()
    aux = pila()
    cargar_pila_random(nums)
    nums.barrido_pila()

    while(not nums.pila_vacia()):
        num = nums.desapilar()
        if (num % 2 != 0):
            aux.apilar(num)

    while(not aux.pila_vacia()):
        num = aux.desapilar()
        nums.apilar(num)

    nums.barrido_pila()

def reemplazar(buscado, suplente): # ok
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

def invertir_pila(): #fail! nosecomocarajoshacerlo :D
    duracell = pila()
    aux_pila =pila()
    cargar_pila_random(duracell)

    rollback = 1
    j = duracell.tamanio()
    for i in range(j):
        while (not duracell.pila_vacia()):
            dato = duracell.desapilar()
            aux_pila.apilar(dato)
            if duracell.tamanio() == rollback:
                dato = duracell.desapilar()
                rollback += 1
                break
        while(not aux_pila.desapilar()):
            aux_dato =aux_pila.desapilar()
            duracell.apilar = aux_dato
            if (aux_pila.tamanio()< (j-1) ):
                aux_pila.apilar(dato)

def palindromo(word): # ok
    palabra = pila()
    inv_palabra=pila()
    
    for i in range(len(word)):
        palabra.apilar(word[i:i+1])
    for i in range(len(word)):
        dato = palabra.desapilar()
        inv_palabra.apilar(dato)

    for i in range(len(word)):
        palabra.apilar(word[i:i+1])        
    
    ac = 0
    while not palabra.pila_vacia():
        if (palabra.desapilar() == inv_palabra.desapilar()):
            ac += 1

    if ac == len(word):
        print("Es palindromo")
    else:
        print("No es palindromo")

def ordenar():
    pilaA = pila()
    pilaB = pila()
    cargar_pila_random(pilaA)
    pilaA.barrido_pila()
    orden = False
    while (not orden):
        while (not pilaA.pila_vacia()):
            dato1 = pilaA.desapilar()
            print (dato1)
            dato2 = pilaA.desapilar()
            if (dato1 >= dato2):
                orden=False
                pilaB.apilar(dato1)
                pilaB.apilar(dato2)
            else:
                orden=True
                pilaB.apilar(dato2)
                pilaB.apilar(dato1)






#buscado = int(input("ingresa algo wey: "))
#ocurrencias(buscado)
eliminar_pares()
#reemplazar(3,5)
#invertir_pila()

#word = str(input())
#palindromo(word)
#ordenar()
