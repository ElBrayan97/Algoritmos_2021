class Pila(object):
#EL DOBLE __ HACE QUE EL OBJETO/VARIABLE SEA DE TIPO PRIVADO#

    def __init__(self): # constructor de la pila 
        self.__elementos = []

    def apilar(self, element): # apila un elemento
        self.__elementos.append(element)

    def desapilar(self): # desapila el elemento de la cima
        return (self.__elementos.pop())

    def pila_vacia(self): # devuelve si la pila esta vacia
        return (len(self.__elementos) == 0)

    def tamanio(self): # devuelve el tamanio de la pila
        return (len(self.__elementos))

    def elemento_cima(self): # devuelve el elemento de la cima de la pila
        return self.__elementos[-1]



    def barrido_pila(self): # realiza un barrido de la pila y la reconstruye
        paux = Pila()
        while (not Pila.pila_vacia(self)):
            dato = Pila.desapilar(self)
            print(dato)
            paux.apilar(dato)
        
        while (not paux.pila_vacia()):
            dato = paux.desapilar()
            self.apilar(dato)