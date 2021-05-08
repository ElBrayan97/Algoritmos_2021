from TDA_Pila import pila
from random import randint

## FUNCIONES DE CARGA ##
def cargar_pila_random(pila): # funcion para cargar elementos random a una pila
    pila.apilar(randint(0, 10))
    pila.apilar(randint(0, 10))
    pila.apilar(randint(0, 10))
    pila.apilar(randint(0, 10))
    pila.apilar(randint(0, 10))

def cargar_bitacoras(pila1,pila2):
    pila1.apilar("Boba Fett", "planeta1","captura2",100)
    pila1.apilar("Boba Fett", "planeta3","captura1",200)
    pila1.apilar("Boba Fett", "planeta7","captura3",500)
    pila2.apilar("Din Djarin", "planeta2","captura6",700)
    pila2.apilar("Din Djarin", "planeta3","captura4",200)
    pila2.apilar("Din Djarin", "planeta5","captura5",300)

def cargar_personajes(pila1,pila2):
    pila1.apilar("otro2")
    pila1.apilar("Din Djarin")
    pila1.apilar("Buba Feet")
    pila2.apilar("otro")
    pila2.apilar("Buba Feet")
    pila2.apilar("Din Djarin")
## FUNCIONES DE CARGA ##

## EJERCICIOS ##
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
    pila_1 = pila()
    pila_aux =pila()
    cargar_pila_random(pila_1)
    pila_1.barrido_pila()
    control = 0

    while ((pila_1.tamanio()) > control):
        dato = pila_1.desapilar()
        while (pila_1.tamanio() != control) or (not pila_1.pila_vacia()):
            pila_aux.apilar(pila_1.desapilar)
        pila_1.apilar(dato)
        control += 1
        while not pila_aux.pila_vacia():
            pila_1.apilar(pila_aux.desapilar())

    print("reordenada")
    pila_1.barrido_pila()


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

def ordenar(): # 14 Esta cosa fea no anda >:V
    pilaA = pila()
    pilaB = pila()
    cargar_pila_random(pilaA)
    pilaA.barrido_pila()
    orden = False
    while (not orden):
        while (not pilaA.pila_vacia()):
            dato1 = pilaA.elemento_cima()
            print (dato1)
            dato2 = pilaA.elemento_cima()
            if (dato1 >= dato2):
                orden=False
                pilaB.apilar(dato1)
                pilaB.apilar(dato2)
            else:
                orden=True
                pilaB.apilar(dato2)
                pilaB.apilar(dato1)

def personajes(): #16
    V, VII, Aux1, Aux2, coincidencias = pila(), pila(), pila(), pila(), pila()
    cargar_personajes(V,VII)
    while not V.pila_vacia():
        personaje = V.desapilar()
        while not VII.pila_vacia():
            personaje2 = VII.desapilar()

            if (personaje == personaje2):
                coincidencias.apilar(personaje)
            Aux2.apilar(personaje2)   

        while not Aux2.pila_vacia():
            dato = Aux2.desapilar()
            VII.apilar(dato)
    print("Personajes que aparecen en las 2 películas:")
    while not coincidencias.pila_vacia():
        print(coincidencias.desapilar())



def bitacoras(): #22


    nave1 = pila()
    nave2 = pila()
    pila_Aux = pila()
    cargar_bitacoras(nave1, nave2)

    while not nave1.pila_vacia():
        data = nave1.desapilar()
        pila_Aux.apilar(data[1], data[2], data[3], data[4])
    while not pila_Aux.pila_vacia():
        print (pila_Aux.desapilar())    

def personajes_MCU(): #24
    pass

## EJERCICIOS ##



# buscado = int(input("ingresa algo wey: "))
# ocurrencias(buscado)
# eliminar_pares()
# reemplazar(3,5)
invertir_pila()

# word = str(input())
# palindromo(word)
# ordenar()
#personajes()
# bitacoras()
