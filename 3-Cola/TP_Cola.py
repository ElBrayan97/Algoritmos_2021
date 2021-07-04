from TDA_Cola import Cola
from TDA_Pila import pila
from random import randint


## FUNCIONES DE CARGA ##

def vocales(word):  # 1
    palabra, vocales = Cola(), Cola()

    for i in range(0,len(word)):
        element = (word[i:i+1])
        palabra.arribo(element)
    
    for i in range(0, palabra.tamanio()):
        word = palabra.atencion()
        if (word == "a" or word == "e" or word == "i" or word == "o" or word == "u"):
            vocales.arribo(word)
        else:
            palabra.arribo(word)

def invertir(palabra): # 2
    lacola = Cola()
    lapila = pila()

    print ('la palabra es: ' + palabra)

    for i in range(0, len(palabra)):
        lacola.arribo(palabra[i:i+1])

    for i in range(0, lacola.tamanio()):
        lapila.apilar(lacola.atencion())
    lapila.barrido_pila()

    for i in range(0, lapila.tamanio()):
        aux = lapila.desapilar()
        lacola.arribo(aux)

def palindromo(palabra): # 3
    cola1 = Cola()
    pila1 = pila()

    print ('la palabra es: ' + palabra)

    tamword=len(palabra)

    for i in range(0, tamword):
        cola1.arribo(palabra[i:i+1])
        pila1.apilar(palabra[i:i+1])
    ac=0
    for i in range(0, tamword):
        if (cola1.atencion() == pila1.desapilar()):
            ac+=1
        else:
            print ("no es palindromo")
            break
    if (ac==tamword):
        print ("la palabra "+palabra+" es un palindromo")

def primos(): # Esto no ha terminado!
    cola1 = Cola()

    for i in range (0,10):
        cola1.arribo(randint(1,10))

    for i in range(0,cola1.tamanio()):
        aux = cola1.atencion()
        if (aux % 2 == 0 and aux % 3 == 0 and aux % 5 == 0 and aux % 7 == 0):
            cola1.arribo(aux)
        else:
            print (aux)
    print(" ")

    for i in range(0,cola1.tamanio()):
        print (cola1.atencion())

def invertir_pila(A): # 5
    P = pila()
    C = Cola()
    for i in range (0,len(A)):
        print (A[i])
        P.apilar(A[i])

    while not P.pila_vacia():
        C.arribo(P.desapilar())

    for i in range(0,C.tamanio()):
        aux = C.atencion()
        print(aux)
        P.apilar(aux)

def ocurrencias(d): # 6
    C = Cola()
    for i in range(0,10):
        C.arribo(randint(0,10))
    
    cont = 0

    while not C.cola_vacia():
        if C.atencion() == d:
            cont += 1
    if (cont == 0):
        print(d ," no aparece en la cola")
    else:
        print(d ," aparece ",cont," veces en la cola")

def eliminar_pos(element): # 7
    C = Cola()
    for i in range (0,10):
        C.arribo(randint(0,10))
    

    for i in range(0,element+1):
        if (i==element):
            print (C.atencion())
        else:
            C.move_end()

# HACER 11, 12 16 Y 22

#a = int(input())

# vocales("onomatopeya")
# invertir("hola")
# palindromo("ala")
# primos()
#A = [1,2,3,4,5]
# invertir_pila(A)
#ocurrencias(a)
#eliminar_pos(a)
