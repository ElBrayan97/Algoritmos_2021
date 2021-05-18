from os import read
from typing import get_origin
from TDA_Pila import pila
from random import randint

## FUNCIONES DE CARGA ##
def cargar_pila_random(pila): # funcion para cargar elementos random a una pila
    pila.apilar(randint(0, 10))
    pila.apilar(randint(0, 10))
    pila.apilar(randint(0, 10))
    pila.apilar(randint(0, 10))
    pila.apilar(randint(0, 10))
    pila.barrido_pila();
    print("fin barrido")

def cargar_bitacoras(pila1, pila2):

        a = ["planeta1","captura2",100]
        pila1.apilar(a)
        a = ["planeta3","captura1",200]
        pila1.apilar(a)
        a = ["planeta7","captura3",500]
        pila1.apilar(a)

        a = ["planeta2","captura6",700]
        pila2.apilar(a)
        a = ["planeta3","captura4",200]
        pila2.apilar(a)
        a = ["planeta5","Han Solo",300]
        pila2.apilar(a)
        a = ["planeta6","captura6",300]
        pila2.apilar(a)

def cargar_personajes(pila1,pila2):
    pila1.apilar("Luke Skywalker")
    pila1.apilar("Han Solo")
    pila1.apilar("Leia Organa")
    pila1.apilar("Darth Vader")
    pila1.apilar("R2-D2")
    pila1.apilar("Lando Calrissian")
    pila1.apilar("C-3PO")
    pila1.apilar("Chewbacca")

    pila2.apilar("Han Solo")
    pila2.apilar("Leia Organa")
    pila2.apilar("Rey")
    pila2.apilar("Finn")
    pila2.apilar("Kylo Ren")
    pila2.apilar("Poe Dameron")
    pila2.apilar("Maz Kanata")
    pila2.apilar("Luke Skywalker")
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

def invertir_pila(): #ok (me costo una banda!!! WTF!)
    pila_1 = pila()
    pila_aux = pila()
    cargar_pila_random(pila_1)
    for i in range (0, pila_1.tamanio()):
        dato = pila_1.desapilar()
        while (pila_1.tamanio() != i):
            aux = pila_1.desapilar()
            pila_aux.apilar(aux)
        pila_1.apilar(dato)
        while (not pila_aux.pila_vacia()):
            aux = pila_aux.desapilar()
            pila_1.apilar(aux)
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
    orden = False
    continuar = 'si'

    while ((continuar.lower) != 'si'):
        num = int(input('Ingrese un numero: '))

        while (not orden):
            if (pilaA.pila_vacia()):
                pilaA.apilar(num)
                orden = True                
            else:
                dato = pilaA.desapilar()
                if (num >= dato):
                    pilaA.apilar(num)
                    pilaA.apilar(dato)
                    orden = True
                else:
                    pilaB.apilar(dato)
                    orden = False
            
            for i in range(0, (pilaB.tamanio()-1)):
                aux = pilaB.desapilar()
                pilaA.apilar(aux)

        print('barrido A')
        pilaA.barrido_pila()
        print('barrido B')
        pilaB.barrido_pila()
        continuar = str(input('Continuar Cargando?... '))        

def personajes(): #16 ok
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
    print("Personajes que aparecen en los 2 capítulos:")
    while not coincidencias.pila_vacia():
        print(coincidencias.desapilar())

def bitacoras(): #22
    CG_1 = 0
    CG_2 = 0
    N_mision = 0
    Han = False

    BobaFett = pila()
    DinDjarin = pila()
    pila_Aux = pila()
    cargar_bitacoras(BobaFett, DinDjarin)
    print (' ')
    print('planetas visitados(mas antiguo a mas reciente): ')

    print('Boba Fett: ')
    while not BobaFett.pila_vacia():
        aux = BobaFett.desapilar()
        pila_Aux.apilar(aux)

    while not pila_Aux.pila_vacia():
        aux = pila_Aux.desapilar()
        print (aux[0])
        if aux[1]=='Han Solo':
            Han = True       
        CG_1 = (CG_1 + aux[2])
        N_mision +=1
        BobaFett.apilar(aux)

    print ('Cantidad de Misiones: ', N_mision, '  Créditos Obtenidos: ',CG_1)
    if Han == True:
        print ('Boba Fett capturo a Han Solo')
        Han = False

    print (' ')

    print('Din Djarin: ')
    while not DinDjarin.pila_vacia():
        aux = DinDjarin.desapilar()
        pila_Aux.apilar (aux)

    N_mision = 0
    while not pila_Aux.pila_vacia():
        aux = pila_Aux.desapilar()
        print (aux[0])
        if aux[1]=='Han Solo':
            Han = True
        CG_2 = (CG_2 + aux[2])
        N_mision +=1
        DinDjarin.apilar(aux)

    print ('Cantidad de Misiones: ', N_mision, '  Créditos Obtenidos: ',CG_2)
    if Han == True:
        print ('Din Djarin capturo a Han Solo')
  
    print (' ')

    if CG_2 > CG_1:
        print ('Din Djarin gano mas créditos')
    elif (CG_2 == CG_1):
        print ('Ambos ganaron lo mismo')
    else:
        print ('Boba Fett gano mas créditos')

    str(input())

def personajes_MCU(): #24
    pass


## EJERCICIOS ##



# buscado = int(input("ingresa algo wey: "))
# ocurrencias(buscado)
# eliminar_pares()
# reemplazar(3,5)
# invertir_pila()

# word = str(input())
# palindromo(word)
#ordenar()


# personajes()
bitacoras()
