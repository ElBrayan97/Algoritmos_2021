class Lista(object):
    """crea un objeto de tipo lista"""

    def __init__(self):
        self.__elementos = []
    
    def __criterio(self, dato, criterio):
        if(criterio == None):
            return dato
        else:
            return dato[criterio]

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


    def modificar_elemento(self, pos, nuevo_valor):
        self.__elementos.pop(pos)
        self.insertar(nuevo_valor)

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

        # [1, 2, 3, 4, 4, 4, 5, 6,7]
    
    def obtener_elemento(self, pos):
        if(pos >= 0 ):
            return self.__elementos[pos]
        else:
            return None

    def lista_vacia(self):
        return len(self.__elementos) == 0
    
    def tamanio(self):
        return len(self.__elementos)

    def barrido(self):
        for elemento in self.__elementos:
            print(elemento)
    
    def barrido_jedi(self):
        for elemento in self.__elementos:
            print(elemento['name'])
    
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
    
    def ordenar(self, criterio):
        quicksort(self.__elementos, 0, len(self.__elementos)-1, criterio)
