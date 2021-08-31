class Arbol(object):

    def __init__(self, dato=None):
        self.dato = dato
        self.izq = None
        self.der = None

    def arbol_vacio(self):
        return self.info is None

    def insertar_Nodo(self, dato):
        if (self.info is None):
            self.info = dato
        elif(dato < self.info):
            if (self.izq is None):
                self.izq = Arbol(dato)
            else:
                self.izq.insertar_Nodo(dato)
        else:
            if self.der is None:
                self.der = Arbol(dato)
            else:
                self.der.insertar_Nodo(dato)

def inorden(self):
    if (self.info is not None):
        if (self.izq is not None):
            self.izq.inorden()
        print(self.info)
        if (self.der is not None):
            self.der.inorden()


def preorden(self):
    if (self.info is not None):
        print(self.info)
        if (self.izq is not None):
            self.izq.preorden()
        
        if (self.der is not None):
            self.der.preorden()


def postorden(self):
    if (self.info is not None):
        if (self.der is not None):
            self.der.postorden()
        print(self.info)
        if (self.izq is not None):
            self.izq.postorden()

def eliminar_nodo(self, dato): # por mis huevos que esto no anda...
    x=None
    if self.info is not None:
        if dato < self.info:
            x = self.izq.eliminar_nodo(self.der, dato)
        elif (dato > self.info):
            x = self.izq.eliminar_nodo(self.der, dato)
        else:
            x = self.info
            if self.izq is None:
                self.info = self.der
            elif self.der is None:
                self.info = self.izq
            else:
                self.izq, x = remplazar(self.izq)
                self.info, self.nrr = x.info, x.nrr




def remplazar(self, dato, reemplazo):
    aux = None
    





arbol = Arbol()

arbol.insertar_Nodo(7)
arbol.insertar_Nodo(10)
arbol.insertar_Nodo(1)
arbol.insertar_Nodo(15)
arbol.insertar_Nodo(5)


#print (arbol.dato, arbol.izq, arbol.der)
#print (arbol.arbol_vacio)