class Lista(object):
    """crea un objeto de tipo lista"""

    def __init__(self):
        self.__elementos = []


    def __criterio(self, dato, criterio):
        if(criterio == None):
            return dato
        else:
            return dato[criterio]


    # esta insercion funciona para listas y diccionarios
    def insertar(self, dato, criterio=None): #! tener en cuenta que la insercion es ordenada
        if(len(self.__elementos) == 0):
            self.__elementos.append(dato)
        elif(self.__criterio(dato, criterio) < self.__criterio(self.__elementos[0], criterio)):
            self.__elementos.insert(0, dato)
        else:
            pos = 0
            while(pos < len(self.__elementos) and self.__criterio(dato, criterio)>=self.__criterio(self.__elementos[pos], criterio)):
                pos +=1 
            self.__elementos.insert(pos, dato) 


    def eliminar(self, dato, criterio=None, clave=None, criterio_clave=None):
        pos = self.busqueda(dato, criterio, clave, criterio_clave)
        if(pos != -1):
            return self.__elementos.pop(pos)
        else:
            return None

    def eliminarTodo(self):
        self.__elementos.clear()

    def eliminar_primero(self): # se fija en el primer elemento de la lista y lo devuelve
        return (self.__elementos.pop(0))


    def modificar_elemento(self, pos, nuevo_valor): # se fija en un elemento en "pos" y lo modifica por "nuevo valor"
        self.__elementos.pop(pos)
        self.insertar(nuevo_valor)

    def reordenar(self,criterio):
        auxiliar = []
        while not self.lista_vacia():
            auxiliar.append(self.__elementos.pop())
        for dato in auxiliar:
            self.insertar(dato,criterio)



    def busqueda(self, buscado, criterio=None, clave=None, criterio_clave=None):
        pos = -1
        primero = 0
        ultimo = len(self.__elementos) -1
        while(primero <= ultimo and pos == -1):
            medio = (primero + ultimo) // 2
            if(self.__criterio(self.__elementos[medio], criterio) == buscado):
                pos = medio
            elif(self.__criterio(self.__elementos[medio], criterio) > buscado):
                ultimo = medio -1
            else:
                primero = medio + 1

        if(pos != -1 and clave is not None and self.__elementos[pos][criterio_clave] != clave):
            while(self.__criterio(self.__elementos[pos], criterio) == self.__criterio(self.__elementos[pos-1], criterio)):
                pos -= 1
            
            while(self.__elementos[pos][criterio_clave] != clave and 
                self.__criterio(self.__elementos[pos], criterio) == self.__criterio(self.__elementos[pos+1], criterio)):
                pos += 1
            
            if(self.__elementos[pos][criterio_clave] != clave):
                pos = -1
        return pos


    def obtener_elemento(self, pos):
        if(pos >= 0 ):
            return self.__elementos[pos]
        else:
            return None


    def lista_vacia(self):
        return (len(self.__elementos) == 0)


    def tamanio(self):
        return len(self.__elementos)


    def barrido(self):
        for elemento in self.__elementos:
            print(elemento['name'])
            #return(elemento)


    def barrido_jedi(self):
        for elemento in self.__elementos:
            return(elemento['name'])


    def barrido_green(self):
        for elemento in self.__elementos:
            if('green' in elemento['lightsaber_color']):
                print(elemento['name'])


    def barrido_lista_autos(self):
        for elemento in self.__elementos:
            print(elemento)
            print('autos:')
            elemento['autos'].barrido()

    # def barrido(self):
    #     for elemento in self.__elementos:
    #         for valor in elemento.values():
    #             print(valor)


    def barrido_eliminando(self, datos_eliminar):
        for elemento in self.__elementos:
            if(elemento in datos_eliminar):
                self.__elementos.remove(elemento)


#    def ordenar(self, criterio):
#        quicksort(self.__elementos, 0, len(self.__elementos)-1, criterio)

