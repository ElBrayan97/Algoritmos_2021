from TDA_Pila import pila

def ejercicio_1(buscado):
    element = pila()
    elementos_aux = pila()

    element.apilar(1)
    element.apilar(2)
    element.apilar(5)
    element.apilar(4)
    element.apilar(5)

    cont = 0
    while(not element.pila_vacia()):
        dato = element.desapilar()
        if (dato == buscado):
            cont += 1
        elementos_aux.apilar(dato)
    print(cont)


buscado = int(input("ingresa algo wey: "))
ejercicio_1(buscado)