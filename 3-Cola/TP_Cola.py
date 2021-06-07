from typing import ValuesView
from TDA_Cola import Cola
from TDA_Pila import pila

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

def invertir(palabra):
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
        print (aux)
        lacola.arribo(aux)




#HACER 11, 12 16 Y 22

#vocales("onomatopeya")

invertir("nomatopeya")