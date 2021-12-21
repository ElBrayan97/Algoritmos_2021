from TDA_Cola import Cola
from TDA_Lista import Lista

class Arbol (object):

    def __init__(self, info = None, datos = None, frecuencia = None):
        self.info = info
        self.datos = datos 
        self.frecuencia = frecuencia
        self.der = None
        self.izq = None
        self._altura = 0

    def arbol_vacio(self):
        """Devuelve True si el arbol vacio."""
        return self.info is None

    def altura (self, arbol):
        """Devuelve la altura de un nodo."""
        if (arbol is None):
            return -1
        else:
            return arbol._altura

    def actualizar_altura (self):
        """Actualiza la altura de un nodo."""
        if (self is not None):
            alt_izq = self.altura(self.izq)
            alt_der = self.altura(self.der)
            self._altura = (alt_izq if alt_izq > alt_der else alt_der) + 1

    def rotacion_simple (self, control):
        if (control):
            aux = self.izq
            self.izq = aux.der
            aux.der = self
        else: 
            aux = self.der
            self.der = aux.izq
            aux.izq = self
        self.actualizar_altura() 
        aux.actualizar_altura() 
        return aux

    def rotacion_doble (self, control):
        if(control):
            self.izq = self.izq.rotacion_simple(False)
            self = self.rotacion_simple(True)
        else:
            self. der = self.der.rotacion_simple(True)
            self = self.rotacion_simple(False)
        return self

    def balancear(self):
        if(self is not None):
            if(self.altura(self.izq)-self.altura(self.der) == 2):
                if(self.altura(self.izq.izq) >= self.altura(self.izq.der)):
                    self = self.rotacion_simple(True)
                else:
                    self = self.rotacion_doble(True)
            elif(self.altura(self.der)-self.altura(self.izq) == 2):
                if(self.altura(self.der.der) >= self.altura(self.der.izq)):
                    self = self.rotacion_simple(False)
                else:
                    self = self.rotacion_doble(False)
        return self

    def insertar_nodo(self, dato, datos = None): 
        """Inserta un dato clave al árbol y opcionalmente hay un campo datos en el que se puede insertar mas información."""
        if(self.info is None):
            self.info = dato
            self.datos = datos
        elif(dato < self.info):
            if(self.izq is None):
                self.izq = Arbol(dato, datos)
            else:
                self.izq = self.izq.insertar_nodo(dato, datos)
        else:
            if(self.der is None):
                self.der = Arbol(dato, datos)
            else:
                self.der = self.der.insertar_nodo(dato, datos)
        self = self.balancear()
        self.actualizar_altura()
        return self

    def inorden (self):#Esta funcion es la principal para crear los demas in orden.
        """Realiza el barrido inorden del arbol.
        Los elementos se listan en orden ascendente (menor a mayor)."""
        if (self.info is not None):
            if (self.izq is not None):
                self.izq.inorden()
            print (self.info, self.datos)
            if (self.der is not None):
                self.der.inorden()

    def postorden (self):
        """Realiza el barrido postorden del arbol.
        Los elementos se listan en orden descendente (mayor a menor)."""
        if(self.info is not None):
            if(self.der is not None):
                self.der.postorden()
            print(self.info)
            if(self.izq is not None):
                self.izq.postorden()

    def preorden (self):
        """Realiza el barrido preorden del arbol.
        Los elementos se listan en el orden en que fueron cargados."""
        if (self.info is not None):
            print (self.info, self._altura)
            if (self.izq is not None):
                self.izq.preorden()
            if (self.der is not None):
                self.der.preorden()         

    def busqueda (self, clave):
        """Devuelve la direccion del elemento buscado."""
        pos = None
        if (self.info is not None):
            if(self.info == clave):
                pos = self
            elif (clave < self.info and self.izq is not None):
                pos = self.izq.busqueda(clave)
            elif (self.der is not None):
                pos = self.der.busqueda(clave)
        return pos

    def busqueda_proximidad(self, clave):
        if(self.info is not None):
            if(self.izq is not None):
                self.izq.busqueda_proximidad(clave)
            if(self.info[0:len(clave)] == clave):
                print(self.info)
            if(self.der is not None):
                self.der.busqueda_proximidad(clave)


    def reemplazar (self):
        """Determina el nodo que remplazará al que se elimina."""
        aux = None
        if (self.der is None): 
            info = self.info
            datos = self.datos
            if(self.izq is not None):
                self.info = self.izq.info
                self.der = self.izq.der
                self.izq = self.izq.izq
                self.datos = self.izq.datos
            else:
                self.info = None
                self.datos = None
        else:
            info, datos = self.der.reemplazar()
        return info, datos

    def eliminar_nodo (self, clave):
        """Elimina un elemento del árbol y lo devuelve si lo encuentra."""
        info, datos = None, None
        if(self.info is not None):
            if(clave < self.info):
                if(self.izq is not None):
                    info, datos = self.izq.eliminar_nodo(clave)
            elif(clave > self.info):
                if(self.der is not None):
                    info, datos = self.der.eliminar_nodo(clave)
            else:
                info = self.info
                datos = self.datos
                if(self.der is None and self.izq is None):
                    self.info = None
                    self.datos = None
                elif(self.izq is None):
                    self.info = self.der.info
                    self.izq = self.der.izq
                    self.der = self.der.der
                    self.datos = self.datos
                elif(self.der is None):
                    self.info = self.izq.info
                    self.der = self.izq.der
                    self.izq = self.izq.izq
                    self.datos = self.datos
                else:
                    info_aux, datos_aux = self.izq.reemplazar()
                    self.info = info_aux
                    self.datos = datos_aux
        self = self.balancear()
        self.actualizar_altura()
        return info, datos

    def barrido_por_nivel (self):
        """Realiza el barrido por nivel del arbol."""
        pendientes = Cola()
        pendientes.arribo(self)
        while (not pendientes.cola_vacia()):
            nodo = pendientes.atencion()
            print (nodo.info)
            if (nodo.izq is not None):
                pendientes.arribo(nodo.izq)
            if (nodo.der is not None):
                pendientes.arribo(nodo.der)

    def barrido_por_nivel_huff (self):
        """Realiza el barrido por nivel del arbol con codigos de Huffman."""
        pendientes = Cola()
        pendientes.arribo(self)
        while (not pendientes.cola_vacia()):
            nodo = pendientes.atencion()
            print (nodo.info, nodo.frecuencia)
            if (nodo.izq is not None):
                pendientes.arribo(nodo.izq)
            if (nodo.der is not None):
                pendientes.arribo(nodo.der)    

####################FUNCIONES EXTRA################################
#########Funciones EJ 1 (Recuperatorio Parcial 2) ########################################

#Punto 4
    def mostrarDino_792(self,clave):
        pos = self.busqueda(clave)
        if pos :
            print (pos.datos) 

#Punto 5
    def busqueda_Trex(self, clave):
            if(self.info is not None):
                    if(self.info == clave):
                        print(self.datos)
                    if(self.izq is not None):
                        self.izq.busqueda_Trex(clave)
                    if(self.der is not None):
                        self.der.busqueda_Trex(clave)
    
#Punto 6 
    def modificar_dino(self):
        buscado = input('Ingrese El Nombre Completo Del Dinosauro Que Desea Cambiar De La Lista Anterior: ')
        pos = self.busqueda(buscado)
        if  pos:
            self.busqueda(buscado)
            nuevo_nombre = input('Ingrese el nuevo nombre: ')
            nombre, datos = self.eliminar_nodo(buscado)
            datos['nombre'] = nuevo_nombre
            self = self.insertar_nodo(nuevo_nombre, datos)
            print()
        self.inorden()

#Punto 7
    def busqueda_Raptor(self, clave):
        if(self.info is not None):
            if(self.info == clave):
                print('Ubicacion',self.datos['ubicacion'])
            if(self.izq is not None):
                self.izq.busqueda_Raptor(clave)
            if(self.der is not None):
                self.der.busqueda_Raptor(clave)


'''
    #Funcion para punto 5 de Ejercio 15

        def inorden_dinosaurios (self):#Esta funcion es la principal para crear los demas in orden.
            """Realiza el barrido inorden_dinosaurios del arbol.
            Los elementos se listan en orden ascendente (menor a mayor)."""
            if (self.info is not None):
                if (self.izq is not None):
                    self.izq.inorden_dinosaurios()
                if (self.info=='Tyrannosaurus rex'):
                    print (self.info, self.datos)
                if (self.der is not None):
                    self.der.inorden_dinosaurios()
'''